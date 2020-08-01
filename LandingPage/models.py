from django.db import models
from myauth.models import *
# Create your models here.
from django.db.models.signals import post_delete
#from django.dispatch import receive
from django.core.validators import RegexValidator

#this table contain all the councelling releted details
class OnlineCounsellingDetails(models.Model):
    councelling_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=30,null=False,blank=False)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="enter valid phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Free Councelling detail'
        verbose_name_plural='Free Councelling details'

#this table contain all the categories
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Course Category'
        verbose_name_plural='Course Categories'

#this relation contains all the subcategories releted to particuler categories
class SubCategory(models.Model):
    subCat_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Subcategories of Categories'
        verbose_name_plural='Subcategories of Categories'

#this relation contains all the courses releted to particuler subcategory
class Course(models.Model):
    Cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    title=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(blank=False,null=True)
    subCat_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Courses'
        verbose_name_plural='Courses'


#this relation associate a particuler facilitator with particuler course
class offer(models.Model):
    Fid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Details about Courses and Facilitator'
        verbose_name_plural='Details about Courses and Facilitators'

