from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    #path('facilitator/', views.facilitator_page),
    path('facilitator/', views.facilitator_page,name='facilitator'),
    path('facilitator-register/', views.RegisterLoginView.as_view(),name='facilitator-register'),
    path('signupform/', views.signup,name='signupform'),
    # #path('Registration/$', views.facilitatorRegistration,name='Registration'),
 ]