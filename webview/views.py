from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
        return render(request, 'webview/index.html')  
def contentPageView(request) :
        return render(request, 'webview/content.html')
def systemPageView(request) :
        return render(request, 'webview/system.html')