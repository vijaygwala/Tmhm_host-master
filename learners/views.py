from django.shortcuts import render,redirect
from .models import *
# Create your views here.

#landing page's learners page
def learner_page(request):
    return render(request, 'learners/index.html')

def certicate(request):
    return render(request,'learners/dashboard/certificate.html')

def chat(request):
    return render(request,'learners/dashboard/chat1.html')

def index(request):
    return render(request,'learners/dashboard/index.html')

def internships(request):
    return render(request,'learners/dashboard/internships.html')

def liveclasses(request):
    return render(request,'learners/dashboard/liveclasses.html')

def profile(request):
    return render(request,'learners/dashboard/profile.html')

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



 