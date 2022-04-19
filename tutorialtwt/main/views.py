from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id): #id is passed from main/urls.py int:id
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST) #holds all of the info from the form in a dictionary
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        # return HttpResponseRedirect("/%i", %t.id)
        return HttpResponseRedirect(f"/{t.id}")

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

# def v1(response):
#     return HttpResponse("<h1>I like vaginas!</h1>")

# def tob(response):
#     return HttpResponse('<img src="https://i1.sndcdn.com/artworks-Dk7pfTjxEROjimBo-tPUNmw-t500x500.jpg"></img>')

