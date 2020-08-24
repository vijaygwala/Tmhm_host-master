from django.contrib import admin
from .models import *

# Register your models here.
class LearnersAdmin(admin.ModelAdmin):
    list_display=('Lid','name','DOB','phone','status','user')
    list_display_links=['name','DOB','phone','status','user']

class LQueryAdmin(admin.ModelAdmin):
    list_display=('Lid','query','reply','added','updated')

admin.site.register(Learners,LearnersAdmin)
admin.site.register(LQueries,LQueryAdmin)