from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from LandingPage.models import Course,Facilitator,offer,Queries
from .serializers import CourseSerializers,offerSerializers,QueriesSerializer

# Considering request.user has Fid=2.

@csrf_exempt
def courses(request):
    if request.method=='GET':
        courses=offer.objects.filter(Fid=2)
        newlist=[]
        for i in range(0,len(courses)):
            course_details=Course.objects.get(name=courses[i].Cid)
            newlist.append(course_details)
        course_data=CourseSerializers(newlist,many=True)
        # print(course_data.data)
        return JsonResponse(course_data.data,safe=False)

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
        
