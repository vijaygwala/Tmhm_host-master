from django.shortcuts import render,redirect
from LandingPage.models import *    
from facilitators.models import *
from math import ceil
from django.contrib import messages
from .forms import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
from myauth.decoraters import *
from django.http import JsonResponse
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
    
    # learner = Learners.objects.get()
    # print(request.user.learner)
    total_rating = 0
    
    if course.no_of_ratings() != 0:
        total_rating = course.no_of_ratings()

    star_list = course.star_count()
    print('LALALA',int(course.avg_rating()))
    course_video=course.course_video.all()[0]
    facilitator=course.offering.all()[0]
    all_course_of_facilitator = facilitator.offering.all()
    sum_of_avg_ratings = 0
    for i in all_course_of_facilitator: 
        sum_of_avg_ratings += i.avg_rating()
    if all_course_of_facilitator.count() != 0:
        facilitator_rating = sum_of_avg_ratings/all_course_of_facilitator.count()

    month =course.updated.strftime('%b')
    year=course.updated.strftime('%Y')
<<<<<<< HEAD
    similer=Course.objects.filter(subCat_id=course.subCat_id.subCat_id).exclude(Cid=course.Cid)[:3]
    print(similer)
    context={'course':course,'course_video':course_video,'facilitator':facilitator,'month':month,'year':year,'similer':similer}
=======
    similer=Course.objects.filter(subCat_id=course.subCat_id).exclude(Cid=course.Cid)[:3]
    context={'course':course,'course_video':course_video,'facilitator':facilitator,'month':month,'year':year,'similer':similer,
    'avg_rating': course.avg_rating(),
    'int_avg_rating': int(course.avg_rating()),
    'total_rating': total_rating,
    'str5': star_list[4],
    'str4': star_list[3],
    'str3': star_list[2],
    'str2': star_list[1],
    'str1': star_list[0],
    'rated_by_me': course.rating_by_me(request.user.learner),
    'pk': pk,
    'total_leaners_for_this_course': course.enroll.all().count(),
    'facilitator_rating': int(facilitator_rating),
    'float_facilitator_rating': round(facilitator_rating, 1),
    }
>>>>>>> e6028bf94039efe47b8cce33e7956880549648c4
    return render(request, 'LandingPage/course/course.html',context)

def rate_course(request, pk=None):
    print('AAAAAAAAYYYYYYYYYYYYYYYAAAAAAAAAA')
    succ = False
    strs = request.GET.get('star', None)
    print(strs)
    crse = Course.objects.get(pk=pk)
    print(crse)
    try:
        obj = Rating.objects.get(course=crse, lerner=request.user.learner)
        obj.stars = int(strs)
        obj.save()
        print("OLD")
        print(obj)
    except:
        new_obj = Rating(course=crse, lerner=request.user.learner, stars=int(strs))
        new_obj.save()
        print('NEW')
    succ = True
    data = {
        'success': succ
    }
    return JsonResponse(data)
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