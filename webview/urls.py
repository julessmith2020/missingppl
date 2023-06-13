from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPageView, name="index"),
    path("index/", views.indexPageView, name="index"),
    path("content/", views.contentPageView, name="content"),
    path("system/", views.systemPageView, name="system")    
]     
