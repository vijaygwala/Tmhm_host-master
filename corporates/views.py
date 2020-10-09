from django.shortcuts import render,redirect
from LandingPage.models import *
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def corporate_landingPage(request):
    course=Course.objects.all()
    filter_level = request.GET.get('level')
    filter_subcat = request.GET.get('subcat')
    filter_lang = request.GET.get('lang')
    filter_partner = request.GET.get('partner')
    if filter_level and filter_level!="None":
        course=Course.objects.filter(level__icontains=filter_level) & course
    if filter_subcat and filter_subcat!="None":
        course=Course.objects.filter(subCat_id__name=filter_subcat) & course
    if filter_lang and filter_lang!="None":
        course=Course.objects.filter(language__icontains=filter_lang) & course
    if filter_partner and filter_partner!="None":
        course=Course.objects.filter(title=Partners.objects.get(name=filter_partner).Cid) & course
    paginator=Paginator(course.values(),2,orphans=1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'subcat':SubCategory.objects.all(),
        'partners':Partners.objects.all(),
        'course':page_obj,
    }
    print(context)
    return render(request,'corporates/index.html',context)