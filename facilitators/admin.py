from django.contrib import admin
from .models import *

class ExperienceInline(admin.StackedInline):
    model = Experience
    can_delete = False
    verbose_name_plural = 'Experience'
    fk_name = 'facilitator'
class FacilitatorQueriesInline(admin.StackedInline):
    model = FacilitatorQueries
    can_delete = False
    verbose_name_plural = 'Facilitator queries'
    fk_name = 'user'
class ApplicantsAdmin(admin.ModelAdmin):
    inlines = (ExperienceInline,FacilitatorQueriesInline )
    list_display=('Aid','name','phone','email','intrest','status')
    list_select_related = ('facilitator', 'user')


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ApplicantsAdmin, self).get_inline_instances(request, obj)


# class ExperienceAdmin(admin.ModelAdmin):
#     list_display=('Eid','Linkedin_Url','Website_Url','Youtube_Url','RExperience','TExperience','facilitator')
# class FacilitatorQueriesAdmin(admin.ModelAdmin):
#     ist_display=('Qid','query','status','user')
class FacilitatorAdmin(admin.ModelAdmin):
    list_display=('Fid','name','DOB','phone','PAddress','TAddress','profile','Bio','country','state','zipcode','user')

admin.site.register(Facilitator,FacilitatorAdmin)
admin.site.register(Applicants,ApplicantsAdmin)
#admin.site.register(Experience,ExperienceAdmin)
