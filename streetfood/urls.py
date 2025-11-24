"""streetfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from streetfoodapp import customer_views as s
from streetfoodapp import merchant_views as m
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Customer Urls



    path('admin/', admin.site.urls),
    path('',s.index,name="index"),
    path('about/',s.about,name="about"),
    path('menu/',s.menu,name="menu"),
    path('services/',s.services,name="services"),
    path('blog/',s.blog,name="blog"),
    path('contact/',s.contact,name="contact"),
    path('contactpage/',s.contactpage,name="contactpage"),
    path('customer/',s.customer,name="customer"),
    path('customer_regpage/',s.customer_regpage,name="customer_regpage"),
    path('customer_login/',s.customer_login,name="customer_login"),
    path('customer_logout/',s.customer_logout,name="customer_logout"),
    path('reg/',s.reg,name="reg"),
    path('customer_details_display/',s.customer_details_display,name="customer_details_display"),
    path('customer_change_password/',s.customer_change_password,name="customer_change_password"),
    path('customer_delete/<str:email>',s.customer_delete,name="customer_delete"),
    path('customer_edit/<str:email>',s.customer_edit,name="customer_edit"),
    path('customer_update/',s.customer_update,name="customer_update"),
    path('customer_view_food/',s.customer_view_food,name="customer_view_food"),
    path('customer_view_order/',s.customer_view_order,name="customer_view_order"),
    path('customerprofile/',s.customerprofile,name="customerprofile"),
    path('view_menu/<int:id>',s.view_menu,name="view_menu"),
    path('customer_order_food/<int:id>',s.customer_order_food,name="customer_order_food"),
    path('feedback/<int:id>',s.feedback,name="feedback"),
    path('customer_view_feedback/<int:id>',s.customer_view_feedback,name="customer_view_feedback"),
    path('administration/', s.administration, name="administration"),
    path('admin_login/', s.admin_login, name="admin_login"),
    path('admin_profile/', s.admin_profile, name="admin_profile"),
    path('admin_change/', s.admin_change, name="admin_change"),
    path('admin_logout/', s.admin_logout, name="admin_logout"),
    path('admin_view_customers/', s.admin_view_customers, name="admin_view_customers"),
    path('admin_view_merchants/', s.admin_view_merchants, name="admin_view_merchants"),
    path('admin_view_feedback/', s.admin_view_feedback, name="admin_view_feedback"),
    path('admin_view_orders/', s.admin_view_orders, name="admin_view_orders"),
    path('admin_accept_merchant/<int:id>', s.admin_accept_merchant, name="admin_accept_merchant"),
    path('admin_reject_merchant/<int:id>', s.admin_reject_merchant, name="admin_reject_merchant"),
    path('order_cancel/<str:food_id>', s.order_cancel, name="order_cancel"),
    path('customer_order_edit/<int:id>',s.customer_order_edit,name="customer_order_edit"),
    path('customer_order_update/',s.customer_order_update,name="customer_order_update"),
    path('order_delete/<int:id>', s.order_delete, name="order_delete"),
    path('add_address/', s.add_address, name="add_address"),
    path('customer_view_address/', s.customer_view_address, name="customer_view_address"),
    path('customer_address_edit/<int:id>', s.customer_address_edit, name="customer_address_edit"),
    path('customer_address_update/', s.customer_address_update, name="customer_address_update"),
    path('address_delete/<int:id>', s.address_delete, name="address_delete"),
    path('checkout/', s.checkout, name="checkout"),
    path('customer_view_orders/', s.customer_view_orders, name="customer_view_orders"),
    path('customer_view_orders_items/<int:id>', s.customer_view_orders_items, name="customer_view_orders_items"),
    path('cancel_checkout/<int:id>', s.cancel_checkout, name="cancel_checkout"),
    path('customerprofile/', s.customerprofile, name="customerprofile"),

    path('add_notifications/', s.add_notifications, name="add_notifications"),
    path('admin_view_notifications/', s.admin_view_notifications, name="admin_view_notifications"),
    path('delete_notifications/<int:id>', s.delete_notifications, name="delete_notifications"),
    path('customers_view_notifications/', s.customers_view_notifications, name="customers_view_notifications"),
    path('search/', s.search, name="search"),
    path('search_menus/', s.search_menus, name="search_menus"),
    #merchant urls



    path('merchant/', m.merchant, name="merchant"),
    path('merchantprofile/', m.merchantprofile, name="merchantprofile"),
    path('merchant_login/', m.merchant_login, name="merchant_login"),
    path('merchant_regpage/', m.merchant_regpage, name="merchant_regpage"),
    path('merchant_register/', m.merchant_register, name="merchant_register"),
    path('merchant_logout/', m.merchant_logout, name="merchant_logout"),
    path('merchant_details_display/', m.merchant_details_display, name="merchant_details_display"),
    path('merchant_change_password/', m.merchant_change_password, name="merchant_change_password"),
    path('merchant_edit/<str:email>', m.merchant_edit, name="merchant_edit"),
    path('merchant_delete/<str:email>', m.merchant_delete, name="merchant_delete"),
    path('merchant_update/', m.merchant_update, name="merchant_update"),
    path('add_food_court/<int:id>', m.add_food_court, name="add_food_court"),
    path('merchant_view_food/<int:id>', m.merchant_view_food, name="merchant_view_food"),
    path('food_edit/<int:id>', m.food_edit, name="food_edit"),
    path('food_update/', m.food_update, name="food_update"),
    path('merchantprofile/', m.merchantprofile, name="merchantprofile"),
    path('food_delete/<int:id>', m.food_delete, name="food_delete"),
    path('food_order/<int:id>', m.food_order, name="food_order"),
    path('approve_slot/<str:food_id>', m.approve_slot, name="approve_slot"),
    path('reject_slot/<str:food_id>', m.reject_slot, name="reject_slot"),
    path('delivered_slot/<str:food_id>', m.delivered_slot, name="delivered_slot"),
    path('merchant_view_feedback/', m.merchant_view_feedback, name="merchant_view_feedback"),
    path('merchant_view_orders/', m.merchant_view_orders, name="merchant_view_orders"),
    path('feedback_delete/<int:id>', m.feedback_delete, name="feedback_delete"),
    path('accept_checkout/<int:id>', m.accept_checkout, name="accept_checkout"),
    path('reject_checkout/<int:id>', m.reject_checkout, name="reject_checkout"),
    path('delivery_checkout/<int:id>', m.delivery_checkout, name="delivery_checkout"),
    path('merchant_view_order_items/<int:id>', m.merchant_view_order_items, name="merchant_view_order_items"),

    path('merchants_view_notifications/', m.merchants_view_notifications, name="merchants_view_notifications"),

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



