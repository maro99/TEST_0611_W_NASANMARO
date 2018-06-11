from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from education.models import School


def school_list(request):

    school= School.objects.all()

    html=''
    for i in school:
        html= i.name+html
        html='\n'+html

    return HttpResponse(html)


