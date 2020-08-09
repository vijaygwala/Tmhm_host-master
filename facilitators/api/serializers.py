from rest_framework import serializers
from myauth.models import *
from django.contrib.auth import get_user_model
from facilitators.models import *
from LandingPage.models import *


# Councelling  section Serializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name',)
    
 #Facilitator queries serializer  
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields=('name','cat_id')
  
#Facilitator queries serializer  
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('code','title','description','days','months','audience','takeaway','subCat_id')
  
class LiveSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=LiveSession
        fields=('title','description','session_start','session_end','days','session_date','session_duration','video','course')
  