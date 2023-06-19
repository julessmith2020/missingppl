from django.urls import path
from . import views

# we created this webview urls.py in order to have access to the views of the server 
# based on the way a user puts the url online (what goes after localhost:8000/)
urlpatterns = [
    path("", views.indexPageView, name="index"),
    path("index/", views.indexPageView, name="index"),
    path("content/", views.contentPageView, name="content"),
    path("system/", views.systemPageView, name="system"),    
    path('person/<str:personID>', views.personView, name='personView'),   
]     
