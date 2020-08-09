import requests,json
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
from LandingPage.models import Course,Facilitator,offer,Category,SubCategory
from math import ceil



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
    r=requests.get('http://127.0.0.1:8000/facilitator/api/dashboard/explore')
    data=json.loads(r.text)
    context={}
    for i in range(0,len(data)):
        subcategory=SubCategory.objects.get(subCat_id=data[i]['subCat_id'])
        context.setdefault('subcategory',set()).add(subcategory)
    category=[]
    for cat in context['subcategory']:
        val=Course.objects.filter(subCat_id=cat.subCat_id)
        n=len(val)
        nSlides=(n//3)+ceil(n/3-n//3)
        l=[val,range(1,nSlides),n]
        category.append(l)
    context.update({'category':category})
    # print(context)
    return render(request, 'facilitators/Dashboard/explore_courses.html',context)

def facilitator_Dashboard_support_page(request):
    if request.method=='POST':
        query=request.POST['Queries']
        data={
            'query':query
        }
        r=requests.post(url='http://127.0.0.1:8000/facilitator/api/support',data=data)
        return redirect('support1')
    context={
        'data':Queries.objects.all()
    }
    
    return render(request, 'facilitators/Dashboard/support.html',context)



def facilitator_Dashboard_create_course_page(request):
    return render(request, 'facilitators/Dashboard/create_course.html')

def facilitator_Profile_page(request):
    return render(request, 'facilitators/Dashboard/profile.html')

def facilitator_Dashboard_settings_page(request):
    return render(request, 'facilitators/Dashboard/settings.html')

   