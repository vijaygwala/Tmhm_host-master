from rest_framework import generics, permissions
from rest_framework.response import Response
#from knox.models import AuthToken
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
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from LandingPage.models import *
from facilitators.api.serializers import *


# Facilitator Register API
class CreateCourseApi(APIView):
    def get(self, request, *args, **kwargs):
            return render(request, 'facilitators/register/mysignup.html', context)

    def post(self, request, *args, **kwargs):
        file=request.FILES['file']
        details=json.loads(request.data.pop('data')[0])
        print(details)
        print(request.user)
        #subcategory_detail=details.pop('subcategory')
        course_detail=details.pop('course')
        video_detail=details.pop('video')
        video_detail['video']=file
        #course=subcategory_detail.get('subcategory')
        subcat=SubCategory.objects.get(name='Web Development')
        print(subcat)
        ofr={}
        offering=None
        course_detail['subCat_id'] =subcat.subCat_id
        c_code=course_detail.get('code')
        try:
            course=Course.objects.get(code=c_code)
        except Course.DoesNotExist:
            course=None
        if details['svideo']=='true':
            if course is None:
                cs = CourseSerializers(data=course_detail)
                if cs.is_valid(raise_exception=True):
                    ins=cs.save()
                    video_detail['course']=ins.Cid
                    ofr['Cid']=ins.Cid
                    ofr['Fid']=request.user.user.facilitator
                    offering=offer.objects.create(Cid=ofr['Cid'],Fid=ofr['Fid'])
                    offering.save()
                
                vs= LiveSessionsSerializer(data=video_detail)
                if vs.is_valid(raise_exception=True):
                    vs.save()
                return Response({'success':'live session is created with new course'},status=201)
            else:
                video_detail['course']=course.Cid
                vs= LiveSessionsSerializer(data=video_detail)
                if vs.is_valid(raise_exception=True):
                    vs.save()
                return Response({'success':'live session is created'},status=201)
        else:
            if course is None:
                cs = CourseSerializers(data=course_detail)
                if cs.is_valid(raise_exception=True):
                    ins=cs.save()
                    video_detail['course']=ins.Cid
                    ofr['Cid']=ins
                    ofr['Fid']=request.user.user.facilitator
                    offering=offer.objects.create(Cid=ofr['Cid'],Fid=ofr['Fid'])
                    offering.save()
                    
                
                vs= VideoRecordedSerializer(data=video_detail)
                if vs.is_valid(raise_exception=True):
                    vs.save()
                return Response({'success':'recorded video is created with new course'},status=201)
            else:
                video_detail['course']=course.Cid
                vs= VideoRecordedSerializer(data=video_detail)
                if vs.is_valid(raise_exception=True):
                    vs.save()
                return Response({'success':'recorded Video is created'},status=201)

# Considering request.user has Fid=2.

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courses(request):
    if request.method=='GET':
        print(request.user)
        courses=offer.objects.filter(Fid=2)
        newlist=[]
        for i in range(0,len(courses)):
            course_details=Course.objects.get(title=courses[i].Cid)
            newlist.append(course_details)
        course_data=CourseSerializers(newlist,many=True)
        # print(course_data.data)
        return Response(course_data)

@csrf_exempt
def support(request):
    if request.method=='POST':
        serializer=QueriesSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(Fid=Facilitator.objects.get(name='vijay gwala'))
            return JsonResponse(serializer.data)

    if request.method=='GET':
        queries=Queries.objects.filter(Fid=2)
        serializer=QueriesSerializer(queries,many=True)
        return JsonResponse(serializer.data,safe=False)
        
