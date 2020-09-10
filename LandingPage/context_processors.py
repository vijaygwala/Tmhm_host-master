from facilitators.models import *
from LandingPage.models import *
from learners.models import *


def base(request):
    return {
        'cat':Category.objects.all()
        }