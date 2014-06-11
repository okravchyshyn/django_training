from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_new(request):
    return HttpResponse("Add new" )

def edit(request, question_id):
    response = "Edit %s."
    return HttpResponse(response % question_id)

