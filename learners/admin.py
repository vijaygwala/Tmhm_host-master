from django.contrib import admin
from .models import *

# Register your models here.
class Reply_inline(admin.TabularInline):
    model = Reply
    verbose_name_plural = 'Facilitator Replies'
    extra = 1
    list_display=('replies')
    list_display_links=['replies']

class LearnersAdmin(admin.ModelAdmin):
    list_display=('Lid','name','DOB','phone','status','user')
    list_display_links=['name','DOB','phone','status','user']

class LQueryAdmin(admin.ModelAdmin):
    list_display=('Lid','query','reply','added','updated')

<<<<<<< HEAD
=======
class ReviewsAdmin(admin.ModelAdmin):
    list_display=('Cid','Lid','reviews','created_at')
    inlines = (Reply_inline,)



>>>>>>> 101f8f26f9de5159061f445e46bc62597ca7203a
admin.site.register(Learners,LearnersAdmin)
admin.site.register(LQueries,LQueryAdmin)