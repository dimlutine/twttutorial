from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id): #id is passed from main/urls.py int:id
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

# def v1(response):
#     return HttpResponse("<h1>I like vaginas!</h1>")

# def tob(response):
#     return HttpResponse('<img src="https://i1.sndcdn.com/artworks-Dk7pfTjxEROjimBo-tPUNmw-t500x500.jpg"></img>')

