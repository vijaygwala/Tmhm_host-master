from django.shortcuts import render,redirect
from LandingPage.models import *    
from facilitators.models import *
from learners.models import *
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
    user=0
    fac_user=0
    userenrolled=Learners.objects.filter(enrolled=Course.objects.get(Cid=pk))
    try:
        login_user=Learners.objects.get(user=request.user)
        if Learners.objects.get(user=request.user) in userenrolled:
            user=1
        if request.method=='POST':
            review=request.POST['review']
            data=Reviews.objects.create(Cid=Course.objects.get(Cid=pk),Lid=Learners.objects.get(user=request.user),reviews=review)
            data.save()
            return redirect('course',pk)
    except:
        pass
    try:
        if str(offer.objects.get(Cid=pk).Fid.user) == str(request.user):
            fac_user=1
    except:
        pass
    rev=request.POST.get('reply1')
    print(rev)
    if rev!=None:
        freply=request.POST.get('reply')
        data=Reply.objects.create(Rid=Reviews.objects.get(pk=int(rev)),replies=freply)
        print(data)
        data.save()
    reviews=Reviews.objects.filter(Cid=Course.objects.get(Cid=pk))
    context.update({'reviews':reviews,'user':user,'fac_user':fac_user})
    print(context)
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
    return render(request, 'LandingPage/categories/categories.html')

#Landing page tems and services page
def termsandservices(request):
    return render(request, 'LandingPage/terms/terms.html')