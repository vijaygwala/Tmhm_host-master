from django.contrib import admin
from .models import *

# By vijay
admin.AdminSite.site_title = "TMHM PVT LTD"
#admin.AdminSite.index_title = ""
admin.AdminSite.site_header = "TMHM PVT LTD "
#admin.AdminSite.login_template='admin_login.html'
#endVijay

# Register your models here.
# from .models import Signup , OnlineCounselling
# admin.site.register(Signup)
# admin.site.register(OnlineCounselling)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('cat_id','name')
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('subCat_id','name','cat_id')
class CourseAdmin(admin.ModelAdmin):
    list_display=('Cid','name','title','description','subCat_id')
class offerAdmin(admin.ModelAdmin):
    list_display=('Fid','Cid')


admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(offer,offerAdmin)