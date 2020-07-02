from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This gon' be a timer.")

def detail(request, program_id):
    return HttpResponse("You're looking at program %s." % program_id)

def results(request, program_id):
    response = "You're looking at the results of program %s."
    return HttpResponse(response % program_id)

def start(request, program_id):
    return HttpResponse("You're starting a timer on program %s." % program_id)

def stop(request, program_id):
    return HttpResponse("You're stopping a timer on program %s." % program_id)
