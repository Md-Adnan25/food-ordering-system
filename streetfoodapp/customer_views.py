from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from streetfoodapp.models import Contact, Customer, Foodcourt, Merchant, Addcart, Feedback, Admin, Address, Order_Items, Order, Notifications
from streetfoodapp.forms import ContactForms, CustomerForms, FoodcourtForms, AddcartForms, FeedbackForms, AdminForm, \
    AddressForm, OrderForm, OrdersForm, Add_notificationsForm


# Create your views here.
def index(request):
    food = Foodcourt.objects.all()
    return render(request, "index.html", {"foods": food})


def about(request):
    return render(request, "about.html", {})


def menu(request):
    food = Foodcourt.objects.all()
    menu = Foodcourt.objects.all()
    return render(request, "menu.html", {"foods": food, "menus": menu})


def services(request):
    return render(request, "services.html", {})


def blog(request):
    return render(request, "blog.html", {})


def contact(request):
    return render(request, "contact.html", {})


def contactpage(request):
    if request.method == "POST":
        contact = ContactForms(request.POST)
        print('hi')
        if contact.is_valid():
            print(contact.errors)
            contact.save()
            return render(request, "contact.html", {"msg": " Thanks For Contacting Us"})
    return render(request, "contact.html", {"msg":"Invalid Email"})


def customer(request):
    return render(request, "customer.html", {})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session['email'] = email
            return render(request, "customerprofile.html", {"msg": email})
        else:
            return render(request, "customer.html", {"msg": "Invalid Email or Password"})
    return render(request, "customer.html", {"msg": "Invalid Email or Password"})

def customerprofile(request):
    return render(request,"customerprofile.html",{})

def customer_regpage(request):
    return render(request, "customer_regpage.html", {})


def reg(request):
    if request.method == "POST":
        email = request.POST["email"]
        print("hai")
        if Customer.objects.filter(email=email).exists():
            return render(request, "customer_regpage.html", {"msg": " This Email Already Exist Can You Please Try With Another Email"})
        else:
            form = CustomerForms(request.POST)
            print("error:", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, "Successfully Registration")
                    return redirect('/customer')
                except Exception as e:
                    print(e)
                    print("hii")
            return render(request, "customer_regpage.html", {"msg": "REGISTER  IS FAIL"})


def customer_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "customer.html", {})


def customer_details_display(request):
    email = request.session['email']
    customers = Customer.objects.get(email=email)
    print('ram')
    return render(request, "customer_details.html", {"customer": customers})


def is_customer(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False



def customer_change_password(request):
    email = request.session['email']
    if is_customer(request):
        if request.method == "POST":
            password= request.POST["old_password"]
            new_password= request.POST["new_password"]
            if password == new_password:
                return render(request,"customer_change_password.html",{"msg":"Your Old And New Passwords Are Same","email":email})
            try:
                users = Customer.objects.get(email=email,password=password)
                users.password = new_password
                users.save()
                messages.success(request,"Successfully Password Updated")
                return redirect('/customer')
            except Exception as e:
                print(e)
                return render(request,'customer_change_password.html',{"msg":"Invalid Creditinals","email":email})
        return render(request,'customer_change_password.html',{"email":email})
    else:
        return redirect('/customer_change_password')


def customerprofile(request):
    return render(request, "customerprofile.html", {})


def customer_delete(request, email):
    user = Customer.objects.get(email=email)
    user.delete()
    return redirect("/customer_regpage")


def customer_edit(request, email):
    customer = Customer.objects.get(email=email)
    return render(request, "customer_edit.html", {"customer": customer})


def customer_update(request):
    if request.method == "POST":
        print("error:")
        email = request.POST["email"]
        print("hello")
        customer = Customer.objects.get(email=email)
        customer = CustomerForms(request.POST, instance=customer)
        print("error:", customer.errors)
        if customer.is_valid():
            print("error:", customer.errors)
            customer.save()
        return redirect("/customer_details_display")
    return redirect("/customer_details_display")


def customer_view_food(request):
    hotel = Merchant.objects.all()
    return render(request, "customer_view_food.html", {"hotels": hotel})


def view_menu(request, id):
    merchant = Merchant.objects.get(id=id)
    food = Foodcourt.objects.filter(merchant_id=merchant.id)
    print("hii")
    return render(request, "view_menu.html", {"foods": food, "hotel": merchant.hotel, "id": merchant.id})



def customer_order_food(request, id):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    food = Foodcourt.objects.get(id=id)

    if request.method == "POST":
        existing_cart_items = Addcart.objects.filter(customer=customer)

        # Check if there are existing items in the cart from a different hotel
        if existing_cart_items.exists() and not existing_cart_items.filter(food__merchant=food.merchant).exists():
            return render(request, "add_to_cart.html", {
                "msg": "Maximum one hotel's items can be selected in the cart at a time.",
                "customer": customer.id, "food": food.id, "cost": food.cost, "dis": food.discount,
                "merchant": food.merchant.hotel, "foodname": food.foodname, "type": food.type,
                "image": food.image.url
            })

        # Check if the item is already in the cart
        if existing_cart_items.filter(food=food).exists():
            return render(request, "add_to_cart.html", {
                "msg": "This food item is already in the cart.",
                "customer": customer.id, "food": food.id, "cost": food.cost, "dis": food.discount,
                "merchant": food.merchant.hotel, "foodname": food.foodname, "type": food.type,
                "image": food.image.url
            })

        # Add the new item to the cart
        book = AddcartForms(request.POST)
        if book.is_valid():
            book.save()
            return redirect("/customer_view_order")

        # If form is not valid, return with errors
        return render(request, "add_to_cart.html", {
            "errors": book.errors, "customer": customer.id, "food": food.id, "cost": food.cost,
            "dis": food.discount, "merchant": food.merchant.hotel, "foodname": food.foodname,
            "type": food.type, "image": food.image.url
        })

    return render(request, "add_to_cart.html", {
        "customer": customer.id, "food": food.id, "cost": food.cost, "dis": food.discount,
        "merchant": food.merchant.hotel, "foodname": food.foodname, "type": food.type,
        "image": food.image.url

    })


def customer_view_order(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    print("hi11")
    details = Addcart.objects.filter(customer_id=customer.id)
    # totalq = 0
    # totalcost = 0
    # totaldiscount = 0
    # totalcosts = 0
    # for item in details:
    #     totalq = totalq+int(item.cart)
    #     totalcost = totalcost+int(item.cost)
    #     totaldiscount = totaldiscount+int(item.discount)
    #     totalcosts = totalcosts+int(item.finalcost)
    tq = 0
    tc = 0
    td = 0
    fc = 0
    for x in details:
        tq = tq + int(x.cart)
        tc = tc + int(x.cost) * int(x.cart)
        td = td + int(x.discount) * int(x.cart)
    fc = fc + tc - td

    adds = Address.objects.filter(email=email)
    print("ryy")
    return render(request, "customer_view_order.html",
                  {"orders": details, "adds": adds, "totalq": tq, "totalcost": tc,
                   "totaldiscount": td, "totalcosts": fc})


def feedback(request, id):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    merchant = Merchant.objects.get(id=id)
    if request.method == "POST":
        feedback = FeedbackForms(request.POST)
        if feedback.is_valid():
            feedback.save()
            return redirect("/customer_view_feedback/{}".format(merchant.id))
    return render(request, "feedback.html", {"customer": customer.id, "merchant": merchant.id})



def customer_view_feedback(request, id):
    merchant = Merchant.objects.get(id=id)
    feedback = Feedback.objects.filter(merchant_id=merchant.id)
    return render(request, "customer_view_feedback.html", {"feedbacks": feedback, "merchant": merchant.hotel})


def unknownadmin(request):
    return render(request, "administration.html", {})


def administration(request):
    return render(request, "administration.html", {})


def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        admin = Admin.objects.filter(email=email, password=password)
        if admin.exists():
            print("hello")
            request.session["email"] = email
            return render(request, "admin_profile.html", {"msg": email})
        else:
            return render(request, "admin_login.html", {"msg": "Invalid Email or Password"})
    return render(request, "admin_login.html", {"msg": ""})



def admin_profile(request):
    return render(request,"admin_profile.html",{})

def is_admin_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def admin_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "index.html", {})


def admin_change(request):
    email = request.session['email']
    if is_admin_login(request):
        if request.method == "POST":
            password= request.POST["old_password"]
            new_password= request.POST["new_password"]
            if password == new_password:
                return render(request,"admin_change.html",{"msg":"Your Old And New Passwords Are Same","email":email})
            try:
                users = Admin.objects.get(email=email,password=password)
                users.password = new_password
                users.save()
                messages.success(request,"Successfully Password Updated")
                return redirect('/admin_login')
            except Exception as e:
                print(e)
                return render(request,'admin_change.html',{"msg":"Invalid Creditinals","email":email})
        return render(request,'admin_change.html',{"email":email})
    else:
        return redirect('/admin_login')

def admin_view_customers(request):
    customers = Customer.objects.all()
    return render(request, "admin_view_customers.html", {"customers": customers})


def admin_view_merchants(request):
    merchants = Merchant.objects.all()
    return render(request, "admin_view_merchants.html", {"merchants": merchants})


def admin_view_feedback(request):
    feedbacks = Contact.objects.all()
    return render(request, "admin_view_feedback.html", {"feedbacks": feedbacks})


def order_cancel(request, food_id):
    cancel = Addcart.objects.get(id=food_id)
    cancel.stutuss = 4
    cancel.save()
    return redirect("/customer_view_order")


def admin_view_orders(request):
    orders = Order_Items.objects.all()
    return render(request, "admin_view_orders.html", {"orders": orders})



def customer_order_edit(request, id):
    food = Addcart.objects.get(id=id)
    return render(request, "customer_order_edit.html", {"food": food})

def customer_order_update(request):
    global id
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    if request.method == "POST":
        id = request.POST["id"]
        food = Addcart.objects.get(id=id)
        food = AddcartForms(request.POST, request.FILES, instance=food)
        print('hi')
        print(food.errors)
        if food.is_valid():
            print(food.errors)
            food.save()
            foods = Addcart.objects.filter(customer_id=customer.id)
            return redirect("/customer_view_order")
    return render(request, "customer_order_edit.html", {"id": id,"food":food})


def order_delete(request, id):
    food = Addcart.objects.get(id=id)
    food.delete()
    return redirect("customer_view_order")
    # return render(request, "customer_view_order.html", {})





def add_address(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    if request.method == "POST":
        address = AddressForm(request.POST)
        print('hi')
        if address.is_valid():
            print(address.errors)
            address.save()
            return redirect("/customer_view_address")
    return render(request, "add_address.html", {"customer": customer.email})


def customer_view_address(request):
    email = request.session['email']
    address = Address.objects.filter(email=email)
    return render(request, "customer_view_address.html", {"address": address})


def customer_address_edit(request, id):
    address = Address.objects.get(id=id)
    return render(request, "customer_address_edit.html", {"address": address})


def customer_address_update(request):
    if request.method == "POST":
        addressid = request.POST["id"]
        address = Address.objects.get(id=addressid)
        address = AddressForm(request.POST, instance=address)
        print("errors", address.errors)
        if address.is_valid():
            address.save()
            print("hell2.0")
            return redirect("/customer_view_address")
    return redirect("/customer_view_address")


def address_delete(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    return redirect("/customer_view_address")


def checkout(request):
    email = request.session['email']
    adds = Address.objects.filter(email=email)
    cart = Addcart.objects.all()
    tq = 0
    tc = 0
    td = 0
    fc = 0
    email = 0
    vmail = 0
    for x in cart:
        email = x.customer.email
        vmail = x.food.merchant.email
        tq = tq + int(x.cart)
        tc = tc + int(x.cost) * int(x.cart)
        td = td + int(x.discount) * int(x.cart)
    fc = fc + tc - td
    if request.method == "POST":
        print("hello")
        form = OrderForm(request.POST)
        print("errors", form.errors)
        print('hii')
        if form.is_valid():
            print("error:", form.errors)
            x = form.save()
            print("x = ", x.id)
            cart_1 = Addcart.objects.all()
            for item in cart_1:
                Order_Items.objects.create(order=x, food=item.food, cost=item.cost, quantity=item.cart,
                                           discount=item.discount, total=item.finalcost, foodname=item.food.foodname,
                                           email=item.customer.email, vmail=item.food.merchant.email)
            cart_1.delete()
            return redirect("/customer_view_orders")
    return render(request, "checkout.html",
                  {"email": email, "vmail": vmail, "td": td, "tc": tc, "tq": tq, "fc": fc, "adds": adds})


def customer_view_orders(request):
    email = request.session["email"]
    orders = Order.objects.filter(email=email)
    return render(request, "customer_view_orders.html", {"orders": orders})

def customer_view_orders_items(request,id):
    orders = Order_Items.objects.filter(order_id=id)
    return render(request, "customer_view_orders_items.html", {"orders": orders})

def cancel_checkout(request, id):
    orders = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrdersForm(request.POST, instance=orders)
        if form.is_valid():
            orders.status = "Cancelled"
            form.save()
            return redirect("/customer_view_orders")
    return render(request, "cancel_checkout.html", {"orders":orders})


def add_notifications(request):
    if request.method == "POST":
        form =Add_notificationsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("admin_view_notifications")
        return render(request, "add_notifications.html", {})
    return render(request, "add_notifications.html", {})

def admin_view_notifications(request):

    notifications = Notifications.objects.all()


    return render(request, "admin_view_notifications.html", {"notifications":notifications})

def delete_notifications(request,id):


    notifications = Notifications.objects.get(id=id)
    notifications.delete()
    return redirect('/admin_view_notifications')

def customers_view_notifications(request):
    notifications = Notifications.objects.all()
    return render(request, "customers_view_notifications.html", {"notifications":notifications})

def search(request):

    queryval = request.POST["hotels"]


    print("hello", queryval)
    search = Merchant.objects.filter(hotel__contains=queryval) | Merchant.objects.filter(
        address__contains=queryval)
    return render(request, "customer_view_food.html", {"hotels": search})


def search_menus(request):
    queryval = request.POST.get("foods", "")
    food_type = request.POST.get("food_type", "")

    print("Search query:", queryval)
    print("Selected type:", food_type)

    search = Foodcourt.objects.all()

    if queryval:
        search = search.filter(
            foodname__icontains=queryval
        ) | search.filter(categoty__icontains=queryval)

    if food_type and food_type != "All":
        search = search.filter(type__iexact=food_type)

    return render(request, "view_menu.html", {"foods": search, "selected_type": food_type})


def admin_accept_merchant(request, id):
    accept = Merchant.objects.get(id=id)
    accept.status = 'Accepted'
    accept.save()
    return redirect('/admin_view_merchants')


def admin_reject_merchant(request, id):
    reject = Merchant.objects.get(id=id)
    reject.status = 'Rejected'
    reject.save()
    return redirect('/admin_view_merchants')

