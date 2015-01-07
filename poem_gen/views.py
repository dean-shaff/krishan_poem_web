from django.shortcuts import render, render_to_response
from django.template import RequestContext
from poem_gen.models import TextInput
import connect3 

def index(request):

	context = RequestContext(request)

	return render_to_response('poem_gen/index.html', context_instance=context)

# Create your views here.
