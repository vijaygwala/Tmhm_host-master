from .views import *
from django.urls import path


urlpatterns = [
    path('LandingPage/signup/', signup, name='signup'),
    path('user/login/', user_login.as_view(), name="login"),
    path('login/page/', login_page, name="login_page"),
    path('user/logout/', user_logout, name="logout"),
    path('changepassword/', ChangePassword, name="changePassword"),
    path('recoverpassword/<int:pk>/', forgot_password, name="forgotPassword"),
]
 