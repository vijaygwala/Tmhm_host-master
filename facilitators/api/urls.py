from django.urls import path
from . import views

urlpatterns = [
    path('facilitator/api/dashboard/explore', views.courses, name="course"),
    path('facilitator/api/support',views.support,name='support')
 ]