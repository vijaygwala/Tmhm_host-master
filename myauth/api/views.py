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
# Register API
class FacilitatorRegisterAPI(APIView):
    def get(self, request, *args, **kwargs):
        category=Category.objects.all()
        subcategory=SubCategory.objects.all()
        context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm(),'category':category,'subcategory':subcategory}
        return render(request, 'facilitators/register/mysignup.html', context)

    def post(self, request, *args, **kwargs):
    
        f=request.data.pop('facilitator')
        query_input=request.data.pop('fquery')
        # print(f)
        form = RegisterSerializer(data=request.data)
        
        #phone=request.POST.get('phone','')
        #portfolio = request.FILES.get('pro','')
        fquery=FacilitatorQueriesFormSerializer(data=query_input)
        #course=request.POST.getlist('course','')
        # catlist=""
        # for cat in course: 
        #     catlist+=cat+","
        # print(course)
        user=None
        try:
            if form.is_valid(raise_exception=True):
                user=form.save()
                f["facilitator"]=user.id
                query_input['user']=user.id
            #     profile=Profile.objects.get(user=user.id)
            #     profile.phone=phone
            #     #profile.portfolio=portfolio
            #     profile.role=2
            #    #profile.intrest=catlist
            #     profile.save()
            else:
                return Response({"messages":"something went wrong in form save method!"})
        except:
            return Response({'messages': 'Something went Wrong in form !'})
        print(f)
        expform = ExperienceSerializer(data=f)
        
        if expform.is_valid(raise_exception=True):
            expform.save()
        if fquery!=None:
            if fquery.is_valid(raise_exception=True):
                fquery.save()
        return Response({'messages': 'User Created successfully'})


from rest_framework.generics import CreateAPIView
class OnlineCouncelling(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'LandingPage/index.html'
    def post(self, request, *args, **kwargs):
        clForm=onlinecounsellingSerializer(data=request.data)
        if clForm.is_valid(raise_exception=True):
            clForm.save()
            messages.success(self.request, 'Thank You For Choosing Us!')
            redirect('/')
            return Response({})
        else:
            messages.error(self.request, 'Invalid Form Detail')
            redirect('/')
            return Response({})
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)