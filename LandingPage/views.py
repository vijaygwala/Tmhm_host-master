from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'LandingPage/index.html')


def home_page(request):
    pass
    '''if request.method=='POST':
        if request.POST.get("f_name"):
            f_name=request.POST.get('f_name','')
            l_name=request.POST.get('l_name','')
            city=request.POST.get('city','')
            email=request.POST.get('email','')
            phone=request.POST.get('phone','')
            poi=request.POST.get('poi','')
            name = f_name+' '+l_name
            signup = Signup(name=name,city=city,email=email,phone=phone,Poi=poi)
            signup.save()
        if request.POST.get('ocphone'):
            phone = request.POST.get('ocphone','')
            councelling = OnlineCounselling(phone=phone)
            councelling.save()
    return render(request, 'LandingPage/index.html')'''

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