from rest_framework import serializers
from LandingPage.models import Course,Category,SubCategory,offer,Facilitator

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['cat_id','name']
    
class SubCategorySerializers(serializers.ModelSerializer):
    cat_id = serializers.PrimaryKeyRelatedField(read_only=False,queryset=Category.objects.all())
    class Meta:
        model=SubCategory
        fields=['subcat_id','name','cat_id']

class CourseSerializers(serializers.ModelSerializer):
    subCat_id = serializers.PrimaryKeyRelatedField(read_only=False,queryset=SubCategory.objects.all())
    class Meta:
        model=Course
        fields=['Cid','name','title','description','thumbnail','subCat_id']

class offerSerializers(serializers.ModelSerializer):
    Fid=serializers.PrimaryKeyRelatedField(read_only=False,queryset=Facilitator.objects.all())
    Cid=serializers.PrimaryKeyRelatedField(read_only=False,queryset=Course.objects.all())

    class Meta:
        model=offer
        fields=['Fid','Cid']