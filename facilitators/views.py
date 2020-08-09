from django.shortcuts import render , redirect
from facilitators.models import *
from facilitators.forms import *
from django.contrib.auth import authenticate, login, logout
from django.views import View
import random
import string
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import register
from LandingPage.models import *    
from django.views.generic import CreateView
from .mixins import AjaxFormMixin
from django.contrib.auth.decorators import login_required
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


# def signup(request):
#     context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm()}
#     return render(request, 'facilitators/register/mysignup.html',context)

# Facilitator registration code personal details , experience details and facilitator queries without Rest Api
class RegisterLoginView(AjaxFormMixin,View):
    def get(self, request, *args, **kwargs):
        category=Category.objects.all()
        subcategory=SubCategory.objects.all()
        context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm(),'category':category,'subcategory':subcategory}
        return render(request, 'facilitators/register/mysignup.html', context)

    def post(self, request, *args, **kwargs):
        context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm()}
        form = UserForm(request.POST)
        expform = ExperienceForm(request.POST)
        phone=request.POST.get('phone','')
        portfolio = request.FILES['pro']
        fquery=FacilitatorQueriesForm(request.POST)
        course=request.POST.getlist('course','')
        catlist=""
        for cat in course:
            catlist+=cat+","
        print(course)
        user=None
        try:
            if form.is_valid():
                user=form.save()
                profile=Profile.objects.get(user=user.id)
                profile.phone=phone
                profile.portfolio=portfolio
                profile.role=2
                profile.intrest=catlist
                profile.save()
            else:
                raise form.ValidationError("Invalid Email or Password !")
        except:
            messages.error(request, ('Incorrect Email or Password !'))
            return redirect('facilitator-register')
            
       
        try:
            if expform.is_valid():
                ex=expform.save(commit=False)
                ex.facilitator=user
                ex.save()
            else:
                raise expform.ValidationError("Invalid Experience Deatails !")
        except:
            messages.error(request, ('Invalid Experience Deatails !'))
            return redirect('facilitator-register')

        if fquery!=None:
            try:
                if fquery.is_valid():
                    qo=fquery.save(commit=False)
                    qo.user=user
                    qo.save()
                else:
                    raise fquery.ValidationError("Invalid Query Deatails !")
            except:
                messages.error(request, ('Invalid Query Deatails !'))
                return redirect('facilitator-register')
       
        messages.success(request, ('Your profile was successfully Created!'))
        
        return redirect('facilitator-register')

def facilitator_Dashboard_Landing_page(request):

    appli = Applicants.objects.get(user=request.user)   #appli.Aid
    approved = Facilitator.objects.get(user=appli)
    context = {'approved':approved}

    return render(request, 'facilitators/Dashboard/index.html',context)
def facilitator_Dashboard_myearnings_page(request):
    return render(request, 'facilitators/Dashboard/my_earnings.html')
def facilitator_Dashboard_explore_courses_page(request):
    return render(request, 'facilitators/Dashboard/explore_courses.html')
def facilitator_Dashboard_support_page(request):
    return render(request, 'facilitators/Dashboard/support.html')



def facilitator_Dashboard_create_course_page(request):
    return render(request, 'facilitators/Dashboard/create_course.html')

def facilitator_Dashboard_settings_page(request):
    return render(request, 'facilitators/Dashboard/settings.html')

class facilitator_login(View):

    def get(self, request):
        return render(request,'facilitators/index.html')


    #authentication_classes = (TokenAuthentication,) 
    #permission_classes = (IsAuthenticated,) 
    def post(self, request):
        if request.method == 'POST':
            email1 =  request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email1, password=password)
            message=None

            try:
                obj = Token.objects.get_or_create(user=user)
                appli = Applicants.objects.get(user=user)   #appli.Aid
                approved = Facilitator.objects.get(user=appli) #aprroved.Fid
                print(obj)
            except:
                obj = None
                approved=None

            if approved:
                if obj:
                    if user:
                        if user.is_active:
                            login(request, user)
                            context = {'approved':approved}
                            return render(request, 'facilitators/Dashboard/index.html', context)
                            return response(obj, status=200)
                        else:
                            return HttpResponse("Account not active")
                    else:
                        print("someone tried to login and failed")
                        return HttpResponse("You are not a facilitator")
                else:
                    return HttpResponse("you are not authorized")
            else:
                return render(request, 'facilitators/index.html')

@api_view(['GET', 'POST'])
def facilitator_Profile_page(request, pk):

    if request.method == 'GET':
        ourdata = Facilitator.objects.get(Fid=pk)   
        ourname = ourdata.name.split()
        firstname = ourname[0]
        lastname = ourname[1]

        context = {'ourdata':ourdata, 'firstname':firstname, 'lastname':lastname,'pk':pk}
        return render(request, 'facilitators/Dashboard/profile.html',context)

    if request.method == 'POST':
        ourdata=Facilitator.objects.get(Fid=pk)
        #profileimg = request.FILES
        #for i in request.FILES:
        if request.FILES:
            ourdata.profile=request.FILES['profile']

        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        ourdata.name=firstname+" "+lastname
        ourdata.phone = request.POST['phone']
        #ourdata.Bio = request.POST['Bio']
        ourdata.country = request.POST['country']
        ourdata.state = request.POST['state']
        ourdata.PAddress = request.POST['addressLine1']
        ourdata.TAddress = request.POST['addressLine2']
        ourdata.zipcode = request.POST['zipCode']
        
        ourdata.save()
        
        context = {'ourdata':ourdata, 'firstname':firstname, 'lastname':lastname,}
        return render(request, 'facilitators/Dashboard/profile.html', context)

    #context = {'ourdata':ourdata}
    return render(request, 'facilitators/Dashboard/profile.html', context)

        
        



   