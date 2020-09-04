from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home,),
    path('aboutus/', views.aboutus),
    path('Courses/Cart/', views.cart,name='cart'),
    path('contact/', views.contact,name='contactus'),
    path('categories/', views.category,name='category'),
    path('terms-and-services/', views.termsandservices),
    path('Free/', views.freecontent,name="freecontent"),
    path('explore/courses/', views.exploreCourses,name='Lexplorecourses'),
    path('course/<int:pk>/', views.CoursePage,name="course"),
    path('rate_course/<int:pk>/', views.rate_course, name="rate_course"),
]
