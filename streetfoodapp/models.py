from datetime import datetime

from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    contactemail=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    msg=models.TextField(max_length=500)

    class Meta:
        db_table="contact_table"

class Customer(models.Model):
    fullname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.TextField(max_length=400)

    class Meta:
        db_table="Customer_table"


class Merchant(models.Model):
    fullname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    hotel=models.CharField(max_length=100)
    img=models.ImageField(blank=True, default='No Image')
    address=models.TextField(max_length=400)
    status = models.CharField(max_length=100, default="On Hold")


    class Meta:
        db_table="merchant_table"


class Foodcourt(models.Model):
    merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    foodname=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.ImageField(blank=True, default='No Image')
    cost=models.BigIntegerField()
    discount=models.BigIntegerField()
    description=models.TextField(max_length=100)

    categoty=models.CharField(max_length=100)

    class Meta:
        db_table="food_details"


class Addcart(models.Model):
    food=models.ForeignKey(Foodcourt,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart=models.CharField(max_length=100)
    cost=models.BigIntegerField()
    discount=models.BigIntegerField()
    finalcost=models.BigIntegerField()
    stutuss=models.IntegerField(default=0)
    class Meta:
        db_table="booking_food"


class Feedback(models.Model):
    merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    text=models.TextField(max_length=100)
    star=models.IntegerField()

    class Meta:
        db_table="feedbacks"



class Admin(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "admin"

class Address(models.Model):
    address = models.CharField(max_length=100)
    typeofadd=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Order(models.Model):
    email = models.EmailField()
    mail = models.EmailField()
    quantity = models.BigIntegerField()
    cost = models.BigIntegerField()
    discount = models.BigIntegerField()
    total = models.BigIntegerField()
    address = models.TextField()
    odatetime = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.CharField(max_length=100, default="Pending")
    reason = models.CharField(max_length=100)

    class Meta:
        db_table = 'Order'


class Order_Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Foodcourt, on_delete=models.CASCADE)
    foodname = models.CharField(max_length=100)
    quantity =  models.BigIntegerField()
    cost = models.BigIntegerField()
    discount = models.BigIntegerField()
    total = models.BigIntegerField()
    email = models.EmailField()
    vmail = models.EmailField()


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ndate_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Notifications"
