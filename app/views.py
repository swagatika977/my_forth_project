from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Ankita(request):
    return HttpResponse('<h1><marquee>hi how r u</h1></marquee>')
