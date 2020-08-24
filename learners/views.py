from django.shortcuts import render

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
    return render(request,'learners/dashboard/Support.html')

def tte(request):
    return render(request,'learners/dashboard/tte.html')



 