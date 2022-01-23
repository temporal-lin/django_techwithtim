from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("VALAX VPN")

def v1(response):
    return HttpResponse("<h1>View 1</h1>")
