from django.shortcuts import render
from mailing.views import *

# Create your views here.

def campus_page(request):
    successEmail()
    return render(request, 'campus/index.html')
