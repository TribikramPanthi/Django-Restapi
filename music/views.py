from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from django.http import HttpResponse, Http404
import datetime
import os
#now using temppate instead of hardcoded html tags in the view
from django.template.loader import get_template
from django.template import Context
#now use render shortcut function rather than loading template and rendering it with context
from django.shortcuts import render



class ListSongsView(generics.ListAPIView):
	"""
	Provides a get method handler.
	"""
	queryset=Songs.objects.all()
	serializer_class=SongsSerializer


def hello(request):
	return HttpResponse("Hello world")

def current_datatime(request):
	now=datetime.datetime.now()
	#html="<html><body>It is now %s.</body><html>"%now
	##Now I am using template based view as

	# t=get_template('current-datatime.html')
	# c=Context({'date':now})
	# html=t.render({'date':now})
	# return HttpResponse(html)
	#now do  this task in single line using render shortcut function
	#so process like template loading, context creation, template rendering and Httpresponse creation are all taken care of by the render() call.
	return render(request,'music/current-datatime.html',{'date':now})



def hours_ahead(request, offset):
	try:
		offset=int(offset)

	except ValueError:
		raise Http404()
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	# html="<html><body> In %s hour(s), it will be %s. </body></html>"%(offset,dt)
	# return HttpResponse(html)

	#using render()
	return render(request,'music/hours_ahead.html',{'offset':offset, 'next_time':dt})

