from django.shortcuts import render,redirect
from .models import *
from rest_framework.decorators import api_view
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

#landing page's learners page
def learner_page(request):
    return render(request, 'learners/index.html')

def certicate(request):
    return render(request,'learners/dashboard/certificate.html')

def chat(request):
    return render(request,'learners/dashboard/chat1.html')

def index(request):
    instance = CustomUser.objects.get(email=request.user)
    learner = Learners.objects.get(Lid=1)
    context = {
        "learner":learner,
    }
    return render(request,'learners/dashboard/index.html', context)

def internships(request):
    return render(request,'learners/dashboard/internships.html')

def liveclasses(request):
    return render(request,'learners/dashboard/liveclasses.html')

@api_view(['GET', 'POST'])
def profile(request, pk):

    if request.method == 'GET':
        ourdata = Learners.objects.get(Lid=pk)   
        ourname = ourdata.name.split()
        firstname = ourname[0]
        lastname = ourname[1]

        context = {'ourdata':ourdata, 'firstname':firstname, 'lastname':lastname,'pk':pk}
        return render(request, 'learners/dashboard/profile.html',context)

    if request.method == 'POST':
          
        ourdata=Learners.objects.get(Lid=pk)
        if request.FILES:
            ourdata.profile=request.FILES['profile']

        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        ourdata.name=str(firstname)+" "+str(lastname)
        ourdata.phone = request.POST.get('phone')
        ourdata.country = request.POST.get('country')
        ourdata.state = request.POST.get('state')
        ourdata.PAddress = request.POST.get('addressLine1')
        ourdata.TAddress = request.POST.get('addressLine2')
        ourdata.zipcode = request.POST.get('zipCode')
        try:
            ourdata.Bio = request.POST['bio']
        except MultiValueDictKeyError:
            pass
        
        
        ourdata.save()
        
        context = {'ourdata':ourdata, 'firstname':firstname, 'lastname':lastname,'pk':pk}
        return render(request, 'learners/dashboard/profile.html', context)

    return render(request, 'learners/dashboard/profile.html', context)

def settings(request):
    return render(request,'learners/dashboard/settings.html')

def support(request):
    learner=Learners.objects.get(Lid=1)
    if request.method=='POST':
        query=request.POST['Queries']
        LQueries.objects.create(Lid=learner,query=query)
        return redirect('learner_support')
    context={
        'data':LQueries.objects.filter(Lid=learner).order_by('query')
    }
    return render(request,'learners/dashboard/Support.html',context)

def tte(request):
    return render(request,'learners/dashboard/tte.html')



 