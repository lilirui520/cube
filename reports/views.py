# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse

def all(request):
    return HttpResponse("Hello world")


def mine(request):
    return HttpResponse("Hello world of mine")
