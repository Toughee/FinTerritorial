from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
	return render(request, 'stateselect/index.html')

#def view_name(request):
#	return render_to_response('index.html', locals() context_instance = RequestContext(request))