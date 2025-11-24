from django import forms
from streetfoodapp.models import Contact,Customer,Merchant,Foodcourt,Addcart,Feedback, Admin, Address, Order, Notifications

class ContactForms(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"


class CustomerForms(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"


class MerchantForms(forms.ModelForm):
    class Meta:
        model=Merchant
        fields = ['fullname', 'mobile', 'city', 'email', 'password', 'hotel','img','address']
        # fields="__all__"


class FoodcourtForms(forms.ModelForm):
    class Meta:
        model=Foodcourt
        fields="__all__"


class AddcartForms(forms.ModelForm):
    class Meta:
        model=Addcart
        fields=('customer','cart','cost','discount','finalcost','food' )


class FeedbackForms(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["mail","email","cost","quantity","discount","total","address"]

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ["reason"]


class Add_notificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"
