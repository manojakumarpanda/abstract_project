from django.shortcuts import render
from django.http.response import HttpResponse

# Create your tests here.


def home(request):
    return HttpResponse('<center><h3>Welcome to the abstract model relation for abstract ::</h3></center>')
