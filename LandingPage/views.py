from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'LandingPage/index.html')



def signup(request):
    return render(request, 'LandingPage/signup/signup.html')


def aboutus(request):
    return render(request, 'LandingPage/aboutus/aboutus.html')


def contact(request):
    return render(request, 'LandingPage/contactus/contact.html')


def category(request):
    return render(request, 'LandingPage/categories/categories.html')


def termsandservices(request):
    return render(request, 'LandingPage/terms/terms.html')