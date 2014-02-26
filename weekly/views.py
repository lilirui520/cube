from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    csrf_context = RequestContext(request)
    return render_to_response('index.html', csrf_context)

def about(request):
    csrf_context = RequestContext(request)
    return render_to_response('about.html', csrf_context)