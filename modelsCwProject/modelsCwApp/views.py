from django.shortcuts import render

# Create your views here.

#importing http
from django.http import HttpResponse

#function to test my url
def index(request):
    return HttpResponse("testing 123")