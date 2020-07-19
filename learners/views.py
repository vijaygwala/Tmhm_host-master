from django.shortcuts import render

# Create your views here.


def learner_page(request):
    return render(request, 'learners/index.html')
