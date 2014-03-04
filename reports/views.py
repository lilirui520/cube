# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
from reports.forms import CreateReportForm
from reports.models import Content

def all(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/index')
    return HttpResponse("Hello world")


def mine(request):
    csrf_context = RequestContext(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/index')
    else:
        if request.method == 'POST':
            form = CreateReportForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                c = Content(start_date=cd['start_date'],
                            end_date=cd['end_date'],
                            cur_done=cd['cur_done'],
                            next_goal=cd['next_goal'],
                            comment=cd['comment'],)
                c.author = request.user
                c.save()
                return render_to_response('reports/post_succeed.html', csrf_context)
                pass
            pass
        else:
            form = CreateReportForm()
            return render_to_response('reports/mine.html', { 'form' : form }, csrf_context)
