from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from LandingPage.models import Course,Facilitator,offer
from .serializers import CourseSerializers,offerSerializers

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
