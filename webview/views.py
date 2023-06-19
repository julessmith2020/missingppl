from django.shortcuts import render
from .models import Person

# Create your views here.
# Each of these functions accesses the views of each html file created and displays them through the render function
# the indexPageView view includes a table we inserted from a database; it connects database with the server
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

def personView(request, personID):
        data = Person.objects.filter(
                id=personID
        ).get()
        #filter builds a where clause
        context = {
                'person' : data
        }
        return render(request, 'webview/person.html', context)
