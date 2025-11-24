from django.contrib import admin

# Register your models here.
from streetfoodapp.models import Merchant
from streetfoodapp.models import Customer
from streetfoodapp.models import Contact
from streetfoodapp.models import Foodcourt
from streetfoodapp.models import Addcart
from streetfoodapp.models import Feedback


admin.site.register(Merchant)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Foodcourt)
admin.site.register(Addcart)
admin.site.register(Feedback)
