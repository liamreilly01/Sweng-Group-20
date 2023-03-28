from django.shortcuts import render
from django.http import HttpResponse
from .apps.py import getChatbotOutput
# Create your views here.

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        # process user input and generate chatbot response
        return HttpResponse(getChatbotOutput)
    else:
        # render the initial form
        return render(request, 'index.html')

def specific(request):
        list1 = [1,2,3,4]
        return HttpResponse(list1)


    
