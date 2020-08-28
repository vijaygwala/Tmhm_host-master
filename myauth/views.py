from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from facilitators.forms import *
from django.contrib.auth.models import Group
from django.views.generic import View
from django.contrib.messages import get_messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token

# global signup system
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email= form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            group = Group.objects.get(name='Visiters')
            user.groups.add(group)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'LandingPage/signup/signup.html', {'form': form})

class user_login(View):
    
    def get(self, request):
        context = {}
        storage = get_messages(request)
        for message in storage:
            print('MESSAGE', message)
            if str(message) == 'password_recovered':
                context['password_recovered']='password_recovered'
            elif str(message) == 'invalid_otp':
                context['invalid_otp']='invalid_otp'
            elif str(message) == 'password_not_same':
                context['password_not_same']= 'password_not_same'
            elif str(message) == 'went_wrong':
                context['went_wrong']= 'went_wrong'
            else:
                return HttpResponseRedirect(reverse('login'))

        print(context)

            
        return render(request,'facilitators/index.html', context)


    
    def post(self, request):
        if request.method == "POST":
            email1 =  request.POST['email']
            password = request.POST['password']
            u=None
            try:
                u = get_object_or_404(CustomUser, email=email1)
            except:
                u=None
                context={'user':u}
                return render(request, 'facilitators/index.html', context)

            user = authenticate(request,email=email1, password=password)
            message=None

           
            if user:
                    
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next', None):
                        return HttpResponseRedirect(request.GET['next'])
                    if user.groups.filter(name='Facilitators').exists():
                        return HttpResponseRedirect(reverse('dashboard'))
                    elif user.groups.filter(name='Learners').exists():
                        return HttpResponseRedirect(reverse('learner_index'))
                    else:
                        return HttpResponseRedirect(reverse('home')) 
                        
                else:
                    notification = "Account is Not Active"
                    context = { 'notification': notification,
                            'clss': 'alert-danger'
                            }
                    if user.groups.filter(name='Facilitators').exists():
                        return render(request, 'facilitators/index.html', context)
                    elif user.groups.filter(name='Learners').exists():
                       return render(request, 'learners/index.html', context)
                    else:
                        return render(request, 'LandingPage/index.html', context)
                        
                    
                        # return HttpResponse("Account not active")
            else:
                print("Not registered! login failed")
                context = {
                        'notification': 'Not registered! login failed',
                        'uemail': u.pk
                    }
                if u.groups.filter(name='Facilitators').exists():
                    return render(request, 'facilitators/index.html', context)
                elif u.groups.filter(name='Learners').exists():
                    return render(request, 'learners/index.html', context)
                else:
                    return render(request, 'LandingPage/index.html', context)
                
        #     # else:
        #     #     return HttpResponse("you are not authorized")
        # else:
        #     print("You are not a facilitator")
        #     notification = "You are not a facilitator"
        #     context = {
        #             'notification': notification,
        #             'clss': 'alert-danger',
        #             'uemail': u.pk
        #         }
        
        #     return render(request, 'facilitators/index.html', context)

def user_logout(request):
    
    if request.user.groups.filter(name='Facilitators').exists():
        logout(request)
        return HttpResponseRedirect(reverse('facilitator'))
    elif request.user.groups.filter(name='Learners').exists():
        logout(request)
        return HttpResponseRedirect(reverse('learner_page'))
    else:
        logout(request)
        return HttpResponseRedirect(reverse('home'))

