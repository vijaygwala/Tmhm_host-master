from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('subscription', order,name='subscription'),
    path('confirm_order', create_order, name = 'create_order'),
    path('payment_status', payment_status, name = 'payment_status')
   
]
