from django.http import HttpResponse
# from django.shortcuts import render
from .models import Legislation
from django.template import loader


# Create your views here.

def acts(request):
    mylegislations = Legislation.objects.all().values()
    template = loader.get_template('all_legislations.html')
    context = {'mylegislations': mylegislations, }
    return HttpResponse(template.render(context, request))
    # return render(request, 'all_legislations.html', {'all': mylegislations})
