from django.http import HttpResponse
from .models import Legislation
from django.template import loader
from django.http import JsonResponse #may not be necessary
from rest_framework.response import Response #from tutorial 2
from rest_framework.decorators import api_view #from tutorial 2
from . serializers import * #from tutorial 2, created in serializers.py


def database(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


@api_view(['GET'])
def legislationList(request):
  legislationActs = Legislation.objects.all()
  serializer = LegislationSerializer(legislationActs, many = True)
  return Response(serializer.data)

@api_view(['GET'])
def legislationDetail(request, key):
  legislation = Legislation.objects.get(id=key)
  serializer = LegislationSerializer(legislation, many=False)
  return Response(serializer.data)
