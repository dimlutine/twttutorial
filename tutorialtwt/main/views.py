from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>I like boobies!</h1>")

def v1(response):
    return HttpResponse("<h1>I like vaginas!</h1>")

def tob(response):
    return HttpResponse('<img src="https://i1.sndcdn.com/artworks-Dk7pfTjxEROjimBo-tPUNmw-t500x500.jpg"></img>')

