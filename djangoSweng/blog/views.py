from django.shortcuts import render
from django.http import HttpResponse
from main import getChatbotOutput

# Create your views here.

def index(request):
    return render(request, 'blog/index.html' )

def specific(request):
        list1 = [1,2,3,4]
        return HttpResponse(list1)

def botResponse(request):
    myMessage = request.GET.get('myMessage')
    myResponse = getChatbotOutput(myMessage)
    return HttpResponse(myResponse)



    
