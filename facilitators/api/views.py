from rest_framework import generics, permissions
from rest_framework.response import Response
#from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.renderers import TemplateHTMLRenderer
#from knox.views import LoginView as KnoxLoginView
from myauth.models import *
from LandingPage.models import *
from facilitators.models import *
from django.shortcuts import render , redirect
import json
from django.contrib import messages
from facilitators.forms import *
import io
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.views import View
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from django.core import serializers

# Facilitator Register API
class CreateCourseApi(APIView):
    def get(self, request, *args, **kwargs):
            return render(request, 'facilitators/register/mysignup.html', context)

    def post(self, request, *args, **kwargs):
        file=request.FILES['file']
        details=json.loads(request.data.pop('data')[0])
        print(details)
        return Response({'success':'hello'},status=201)
        #subcategory_detail=details.pop('subcategory')
        course_detail=details.pop('course')
        video_detail=details.pop('video')
        video_detail['video']=file
        #course=subcategory_detail.get('subcategory')
        subcat=SubCategory.objects.get(name='Programming Languages')
        print(subcat)

        course_detail['subCat_id'] =subcat.subCat_id
        c_code=course_detail.get('code')
        try:
            course=Course.objects.get(code=c_code)
        except Course.DoesNotExist:
            course=None
        if course is None:
            cs = CourseSerializer(data=course_detail)
            if cs.is_valid(raise_exception=True):
                ins=cs.save()
                video_detail['course']=ins.Cid
            
            vs= LiveSessionsSerializer(data=video_detail)
            if vs.is_valid(raise_exception=True):
                vs.save()
            return Response({'success':'course is created'},status=201)
        else:
            video_detail['course']=course.Cid
            vs= LiveSessionsSerializer(data=video_detail)
            if vs.is_valid(raise_exception=True):
                vs.save()
            return Response({'success':'Video is created'},status=201)