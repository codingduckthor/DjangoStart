from django.http import HttpResponse
from django.template import loader
from bboard.models import Bb
from django.shortcuts import render

# from django.shortcuts import render

def index(request):
    # template = loader.get_template('index.html')
    bbs = Bb.objects.all()
    context = {'bbs': bbs}

    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)
