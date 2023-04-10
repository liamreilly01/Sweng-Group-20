from django.http import HttpResponse
from .models import Legislation
from django.template import loader
from django.http import JsonResponse #may not be necessary
from rest_framework.response import Response #from tutorial 2
from rest_framework.decorators import api_view #from tutorial 2
from . serializers import * #from tutorial 2, created in serializers.py
from django.shortcuts import render
from database.main import *

flag = False;


def database(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


@api_view(['GET'])
def legislationList(request):
  legislationActs = Legislation.objects.all()
  serializer = LegislationSerializer(legislationActs, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def legislationDetail(request, key):
  legislation = Legislation.objects.get(id=key)
  serializer = LegislationSerializer(legislation, many=False)
  return Response(serializer.data)

def obtainModel(request):
  print("model getting")
  model = getModel()
  return HttpResponse(model)

def obtainMostLikelyAct(request):
  print("api querying")
  MostLikelyAct = getMostLikelyAct(request.GET.get('myMessage'))
  return HttpResponse(MostLikelyAct)


def botResponse(request):
    myMessage = request.GET.get('myMessage')
    pipeline = request.GET.get('pipeline')
    print(pipeline)
    flag = True
    mostLikelyActID = request.GET.get('id')
    mostLikelyActUrl = request.GET.get('url')
    mostLikelyActTitle = request.GET.get('title')
    mostLikelyActDesription = request.GET.get('desription')
    mostLikelyActDetails = request.GET.get('details')
    myResponse = getChatbotOutput(mostLikelyActID, mostLikelyActUrl, mostLikelyActTitle, mostLikelyActDesription, mostLikelyActDetails, pipeline, myMessage)
    return HttpResponse(myResponse)

def index(request):
    return render(request, 'blog/index.html')
