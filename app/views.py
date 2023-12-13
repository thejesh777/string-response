from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def string(request):
    return HttpResponse('this is my frist string response')