from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def index(request):
    project_list = Project.objects.all()
    output = ', '.join([q.project_name_text + " " + q.time_text for q in project_list])
    return HttpResponse(output)

def detail(request, program_id):
    return HttpResponse("You're looking at program %s." % program_id)

def results(request, program_id):
    response = "You're looking at the results of program %s."
    return HttpResponse(response % program_id)

def start(request, program_id):
    return HttpResponse("You're starting a timer on program %s." % program_id)

def stop(request, program_id):
    return HttpResponse("You're stopping a timer on program %s." % program_id)
