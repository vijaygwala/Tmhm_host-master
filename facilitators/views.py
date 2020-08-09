from django.shortcuts import render , redirect
from facilitators.models import *
from facilitators.forms import *
from django.contrib.auth import authenticate,login
from django.views import View
import random
import string
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import register
from LandingPage.models import *



#facilitator page
def facilitator_page(request):
    return render(request, 'facilitators/index.html')



    
from django.views.generic import CreateView
from .mixins import AjaxFormMixin
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
    return render(request, 'facilitators/Dashboard/index.html')
def facilitator_Dashboard_myearnings_page(request):
    return render(request, 'facilitators/Dashboard/my_earnings.html')
def facilitator_Dashboard_explore_courses_page(request):
    category=Category.objects.all()
    subcategory=SubCategory.objects.all()
    context={'category':category, 'subcategory':subcategory}

    return render(request, 'facilitators/Dashboard/explore_courses.html',context)
def facilitator_Dashboard_support_page(request):
    return render(request, 'facilitators/Dashboard/support.html')



def facilitator_Dashboard_create_course_page(request):
    if request.method=='POST':
        pass
    else:
        audience_list=Audience.objects.values('audience')

        context={
            'audience_list':audience_list
        }
        return render(request, 'facilitators/Dashboard/create_course.html',context)

def facilitator_Profile_page(request):
    return render(request, 'facilitators/Dashboard/profile.html')

def facilitator_Dashboard_settings_page(request):
    return render(request, 'facilitators/Dashboard/settings.html')

   