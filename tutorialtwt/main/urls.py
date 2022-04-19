from django.urls import path

#import views from the current director that we're in
from . import views

#if we don't specify a page, we're going to go to index
urlpatterns = [
    # path("", views.index, name="index"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home")
    # path("v1/", views.v1, name="v1"),
    # path("tob/", views.tob, name="tob"),
]