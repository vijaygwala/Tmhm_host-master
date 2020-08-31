from django.shortcuts import render,redirect
from LandingPage.models import *    
from facilitators.models import *
from math import ceil
from django.contrib import messages
from .forms import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
from myauth.decoraters import *
# Landing  page
def home(request):
    return render(request,'LandingPage/index.html')

#free content avialable for users here 
@login_required(login_url='/home')
@allowed_users(['Visiters','Learners','Facilitators'])
def freecontent(request):
    return render(request,'LandingPage/freeContent/index.html')

# users can expolore the courses from explore courses
def exploreCourses(request):
    course=offer.objects.all()
    course1=[]
    context={}
    if len(course)==0:
        context.update({'count':0})
        return render(request,'LandingPage/exploreCourses/exploreCourses.html',context)
    for i in range(0,len(course)):
        subcategory=SubCategory.objects.get(name=course[i].Cid.subCat_id)
        context.setdefault('subcategory',set()).add(subcategory)
        course1.append(course[i].Cid)
    category=[]
    for cat in context['subcategory']:
        val=Course.objects.filter(subCat_id=cat.subCat_id)
        val1=[]
        for c in val:
            if c in course1:
                val1.append(c)
        n=len(val1)
        nSlides=(n//3)+ceil(n/3-n//3)
        l=[val1,range(1,nSlides),n]
        category.append(l)
    print(context)
    context.update({'category':category})
    return render(request,'LandingPage/exploreCourses/exploreCourses.html',context)


#Landing page about us page
def aboutus(request):
    return render(request, 'LandingPage/aboutus/aboutus.html')

#this is course page
def CoursePage(request,pk):
    course=Course.objects.get(Cid=pk)
    course_video=course.course_video.all()[0]
    facilitator=course.offering.all()[0]
    month =course.updated.strftime('%b')
    year=course.updated.strftime('%Y')
    similer=Course.objects.filter(subCat_id=course.subCat_id).exclude(Cid=course.Cid)[:3]
    context={'course':course,'course_video':course_video,'facilitator':facilitator,'month':month,'year':year,'similer':similer}
    return render(request, 'LandingPage/course/course.html',context)

#Landing page Contact us page
def contact(request):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Details Submitted Succesfully")
            return redirect('contactus')
    form=ContactUsForm()
    context={'form':form}
    return render(request, 'LandingPage/contactus/contact.html',context)

#Landing page categories page
def category(request):
    categories=SubCategory.objects.all()[:7]
    pk=request.GET.get('id')
    if pk is None:
        cat = SubCategory.objects.get(subCat_id=categories[0].subCat_id)
    else:
        cat = SubCategory.objects.get(subCat_id=pk)
    
    courses=Course.objects.filter(subCat_id=cat)
    context={'categories':categories,'courses':courses}
    return render(request, 'LandingPage/categories/categories.html',context)

#Landing page tems and services page
def termsandservices(request):
    return render(request, 'LandingPage/terms/terms.html')