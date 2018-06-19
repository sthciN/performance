from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from models import info
from django.utils import timezone

def entry(request):
    return HttpResponse(timezone.now())
# Create your views here.
