from django.shortcuts import render , redirect, get_object_or_404
from facilitators.models import *
from facilitators.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
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
from django.http import JsonResponse
from django.views.generic import View
from passlib.hash import django_pbkdf2_sha256 as handler
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout
import json
from math import ceil
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.conf import settings
import random
import threading
import datetime
from django.template import RequestContext
#facilitator page
def facilitator_page(request):
    return render(request, 'facilitators/index.html')

    
from django.views.generic import CreateView
from .mixins import AjaxFormMixin

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


@login_required(login_url='/facilitator/login/')
def facilitator_Dashboard_Landing_page(request):
   #by saurabh
    print(request.user)
    instance = CustomUser.objects.get(email=request.user)
    # o = instance.learner.all()
    # print('leaner', o)
    
    
    obj = instance.user.facilitator
    total_queries = Queries.objects.filter(Fid=obj.Fid).count()
    # print(total_queries)
    pro = instance.user
    offr = offer.objects.filter(Fid=obj.Fid)
    # print(offr)
    total_course = offr.count()
    total_learners = 0
    active_learners = 0
    for course in offr: 
        active_learners += course.Cid.enroll.filter(status="Active").count()
        total_learners += course.Cid.enroll.all().count()
    
    if total_learners != 0:
        active_learners = (active_learners/total_learners)*100

    context = {
        "facilitator_name" : obj.name,
        "Bio" : obj.Bio,
        "courses": offr,
        "total_course": total_course,
        "profile_id": obj.Fid,
        "intrest": pro.intrest,
        'total_learners': total_learners,  
        'active_learners': active_learners,
        'total_queries': total_queries
    }
    # My courses
    appli=Applicants.objects.get(user=request.user)
    faci=Facilitator.objects.get(user=appli)
    course=offer.objects.filter(Fid=faci.Fid)
    if len(course)==0:
        context.update({'count':0})
        return render(request,'facilitators/Dashboard/index.html',context)
    category=[]
    val1=[]
    for cat in course:
        val=Course.objects.get(code=cat.Cid.code)
        val1.append(val)
    n=len(val1)
    nSlides=(n//3)+ceil(n/3-n//3)
    context.update({'courses':val1})
    context.update({'nSlides':nSlides})
    context.update({'range':range(1,nSlides)})
    print(context)
    # by aamir
    appli = Applicants.objects.get(user=request.user)   #appli.Aid
    approved = Facilitator.objects.get(user=appli)
    context['approved'] = approved

    return render(request, 'facilitators/Dashboard/index.html',context)


@login_required(login_url='/facilitator/login/')
def facilitator_Dashboard_myearnings_page(request):
    return render(request, 'facilitators/Dashboard/my_earnings.html')


@login_required(login_url='/facilitator/login/')
def facilitator_Dashboard_explore_courses_page(request):   
    # r=requests.get('http://127.0.0.1:8000/facilitator/api/dashboard/explore')
    # data=json.loads(r.text)
    # print(request.user.id)
    # data=Facilitator.objects.get(email=request.user)
    # appli=Applicants.objects.get(user=request.user)
    # faci=Facilitator.objects.get(user=appli)
    # course=offer.objects.all()
    # course1=[]
    # context={}
    # if len(course)==0:
    #     context.update({'count':0})
    #     return render(request,'facilitators/Dashboard/explore_courses.html',context)
    # for i in range(0,len(course)):
    #     subcategory=SubCategory.objects.get(name=course[i].Cid.subCat_id)
    #     context.setdefault('subcategory',set()).add(subcategory)
    #     course1.append(course[i].Cid)
    # category=[]
    # for cat in context['subcategory']:
    #     val=Course.objects.filter(subCat_id=cat.subCat_id)
    #     val1=[]
    #     for c in val:
    #         if c in course1:
    #             val1.append(c)
    #     n=len(val1)
    #     nSlides=(n//3)+ceil(n/3-n//3)
    #     l=[val1,range(1,nSlides),n]
    #     category.append(l)
    # print(context)
    # context.update({'category':category})
    # return render(request, 'facilitators/Dashboard/explore_courses.html',context)
    return redirect('Lexplorecourses')


@login_required(login_url='/facilitator/login/')
def facilitator_Dashboard_support_page(request):
    appli=Applicants.objects.get(user=request.user)
    faci=Facilitator.objects.get(user=appli)
    if request.method=='POST':
        query=request.POST['Queries']
        Queries.objects.create(Fid=faci,query=query)
        return redirect('support1')
    context={
        'data':Queries.objects.filter(Fid=faci).order_by('query')
    }
    
    return render(request, 'facilitators/Dashboard/support.html',context)



@login_required(login_url='/facilitator/login/')
def facilitator_Dashboard_create_course_page(request):
    audience_list=Audience.objects.values('audience')
    category=Category.objects.all()
    subcategory=SubCategory.objects.all()
    context={
        'audience_list':audience_list,
        'category':category,
        'subcategory':subcategory
    }
    return render(request, 'facilitators/Dashboard/create_course.html',context)

@login_required(login_url='/facilitator/login/')
def facilitator_Dashboard_settings_page(request):
    return render(request, 'facilitators/Dashboard/settings.html')



class facilitator_login(View):
    
    def get(self, request):
        return render(request,'facilitators/index.html')


    #authentication_classes = (TokenAuthentication,) 
    #permission_classes = (IsAuthenticated,) 
    def post(self, request):
        if request.method == "POST":
            email1 =  request.POST['email']
            password = request.POST['password']
            # print(email1, password)
            u = get_object_or_404(CustomUser, email=email1)
            user = authenticate(request,email=email1, password=password)
            message=None
            try:
                obj = Token.objects.get_or_create(user=user)
                appli = Applicants.objects.get(user=user)  #appli.Aid
                approved = Facilitator.objects.get(user=appli) #aprroved.Fid
            except:
                obj = None
                approved=None
            # print(approved)
            if approved:
                # if obj:
                if user:
                    
                    if user.is_active:
                        login(request, user)
                        # print(" after login")
                        # print(user)
                        # request.user=user
                        # context = {'approved':approved}
                        if request.GET.get('next', None):
                            return HttpResponseRedirect(request.GET['next'])
                        return HttpResponseRedirect(reverse('dashboard'))
                        # return response(obj, status=200)
                    else:
                        notification = "Account not active"
                        context = { 'notification': notification,
                            'clss': 'alert-danger'
                            }
                        return render(request, 'facilitators/index.html', context)
                        # return HttpResponse("Account not active")
                else:
                    print("Not registered! login failed")
                    context = {
                        'notification': 'Not registered! login failed',
                        'uemail': u.pk
                    }
                    return render(request, 'facilitators/index.html', context)
            # else:
            #     return HttpResponse("you are not authorized")
            else:
                print("You are not a facilitator")
                notification = "You are not a facilitator"
                context = {
                    'notification': notification,
                    'clss': 'alert-danger',
                    'uemail': u.pk
                }
                print(context['uemail'])
                return render(request, 'facilitators/index.html', context)


@login_required(login_url='/facilitator/login/')
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

        
        


# for handling ajax request for change password form of setting section of profile
@login_required(login_url='/facilitator/login/')
def ChangePassword(request):
    suc_res = ''
    err_res = ''
    current = request.GET.get('currentPassword', None)
    newp = request.GET.get('newPassword', None)
    confirmp = request.GET.get('confirmNewPassword', None)


    try:
        obj = get_object_or_404(CustomUser, email=request.user)
        # print(obj.password)
    except:
        print('NO USER FOUND')
        # print(handler.verify(current, obj.password))
    if handler.verify(current, obj.password):
        obj.set_password(confirmp)
        obj.save()
        suc_res = 'Password changed successfully!'
    else:
        err_res = "Invalid current Password!"


    msg = { 'err_res':err_res,
            'suc_res': suc_res
        }

    data = {
            'msg': msg
        }
    return JsonResponse(data)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('facilitator'))


# pending forgot password view -------------------------------
def forgot_password(request, pk=None):
    suc = ''
    ms = ''
    print('GETTTTTTTTTTT')
    if request.method == 'GET':
        print(pk)
        u = CustomUser.objects.get(id=pk)
        print(u)
        #get_object_or_404(CustomUser, pk=pk)
        otp = random.randrange(1234, 99999, 3)
        print(otp)
        print(u)
        receiver = 'vijaygwala73@gmail.com'
        subject = 'OTP from Learnopad' + ' : ' + str(otp)
        text = 'Hi '+ receiver+' Your one time password for Learnopad.com is: ' + str(otp) + 'This OTP is valid for 7 minutes only!'
        send_mail(str(subject), text, 'vijaygwala97@gmail.com', [receiver,],fail_silently=False)
        print('mail sent')
        def expire():
            try:
                o = get_object_or_404(OTP, sender=u.email)
                print(o.value)
                print('Deleting OTP...')
                o.delete()
            except:
                print('Already deleted')
        try:
            o = get_object_or_404(OTP, sender=u.email)
            o.value = otp
            o.save()
            threading.Timer(420.0, expire).start()
        except:
            o = OTP.objects.create(sender=u.email, value=otp)
            threading.Timer(420.0, expire).start()


    if request.method == 'POST':
        print('POSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
        u = get_object_or_404(CustomUser, pk=pk)
        o = get_object_or_404(OTP, sender=u.email)
        otp =  request.POST['otp']
        newpassword =  request.POST['newpassword']
        confirmpassword =  request.POST['confirmpassword']
        
        if str(newpassword) == str(confirmpassword):

            if str(o.value) == str(otp):
                print("haiiiiiiiiiiiiiiiiiiii")
                u.set_password(confirmpassword)
                u.save()
                suc = 'alert-success'
                ms = 'Your Password Changed Successfully!'
                return render(request, 'facilitators/index.html', {'repsonse': 'Account recovered Successfully!', 'arg': 'success', 'heading': 'Hurray!'})
            else:
                return render(request, 'facilitators/index.html', {'repsonse':"Invalid or Expired OTP", 'arg': 'error', 'heading': 'Oops!'})
        else:
            return render(request, 'facilitators/index.html', {'repsonse':"Passwords must be same!", 'arg': 'error', 'heading': 'Sorry!'})
    else:
        
        return render(request, 'facilitators/index.html', {'repsonse':"Something went worng! Try again!", 'arg': 'warning', 'heading': 'Sorry'})
