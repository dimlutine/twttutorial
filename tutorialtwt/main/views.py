from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, name): #id is passed from main/urls.py int:id
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse(f'<h1>I like boobies!</h1><p><br /><b>ls.name is</b> {ls.name}<br /><b>item.text is</b> {str(item.text)}</p><br /><img src="https://i1.sndcdn.com/artworks-Dk7pfTjxEROjimBo-tPUNmw-t500x500.jpg"></img>')

# def v1(response):
#     return HttpResponse("<h1>I like vaginas!</h1>")

# def tob(response):
#     return HttpResponse('<img src="https://i1.sndcdn.com/artworks-Dk7pfTjxEROjimBo-tPUNmw-t500x500.jpg"></img>')

