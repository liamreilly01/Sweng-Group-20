from django.http import HttpResponse
from .models import Legislation
from django.template import loader

def database(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
