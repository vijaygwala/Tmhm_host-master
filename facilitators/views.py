from django.shortcuts import render, redirect, get_object_or_404
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
from myauth.models import *
from django.http import JsonResponse
from django.views.generic import View



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
    print(request.user)
    instance = CustomUser.objects.get(email="saurabhpanwar127@gmail.com")
    obj = instance.user.facilitator
    print(obj)
    pro = instance.userprofile
    offr = offer.objects.filter(Fid=obj.Fid)
    total_course = offr.count()
    context = {
        "facilitator_name" : obj.name, 
        "Bio" : obj.Bio,
        "courses": offr,
        "total_course": total_course,
        "intrest": pro.intrest
    }   
    return render(request, 'facilitators/Dashboard/index.html', context)
def facilitator_Dashboard_myearnings_page(request):
    return render(request, 'facilitators/Dashboard/my_earnings.html')
def facilitator_Dashboard_explore_courses_page(request):
    return render(request, 'facilitators/Dashboard/explore_courses.html')
def facilitator_Dashboard_support_page(request):
    return render(request, 'facilitators/Dashboard/support.html')
    


def facilitator_Dashboard_create_course_page(request):
    return render(request, 'facilitators/Dashboard/create_course.html')

def facilitator_Profile_page(request):
    return render(request, 'facilitators/Dashboard/profile.html')

def facilitator_Dashboard_settings_page(request):
    obj = get_object_or_404(CustomUser, email='saurabhpanwar127@gmail.com')
    # obj.set_password(newpasswrd)
    # print('Password is:', obj.password)
    return render(request, 'facilitators/Dashboard/settings.html')


# for handling ajax request for change password form of setting section of profile

class ChangePassword(View):
    def get(self, request):
        response = ''
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAA')
        current = request.GET.get('currentPassword', None)
        newp = request.GET.get('newPassword', None)
        confirmp = request.GET.get('confirmNewPassword', None)
        print('ALALALLALAL')

        try:
            obj = get_object_or_404(CustomUser, email=request.user.email)
            print(obj)
        except:
            print('NO USER FOUND')
        
        if obj.password == current:
            obj.set_password(confirmp)
            response = 'Password changed successfully!'
        
        else:
            response = "Invalid current Password!"


        msg = { 'response':response }

        data = {
                'msg': msg
            }
        return JsonResponse(data)