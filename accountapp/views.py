from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Hello_world(request):
    return render(request, 'base.html')