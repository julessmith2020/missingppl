from django.shortcuts import render
from .models import Person

# Create your views here.
def indexPageView(request) :
        personTable = Person.objects.all()
        context = {
                'personTable' : personTable
        }
        return render(request, 'webview/index.html', context)  
def contentPageView(request) :
        return render(request, 'webview/content.html')
def systemPageView(request) :
        return render(request, 'webview/system.html')