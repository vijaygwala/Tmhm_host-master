from .views import *
from django.urls import path


urlpatterns = [
    path('LandingPage/signup/', signup, name='signup'),
    path('user/login/', user_login.as_view(), name="login"),
    path('user/logout/', user_logout, name="logout"),
    
]
