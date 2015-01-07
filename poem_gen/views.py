from django.shortcuts import render, render_to_response
from django.template import RequestContext
from poem_gen.models import TextInput
from poem_creator import poem_creator

def index(request):

	context = RequestContext(request)

	list_of_objects = TextInput.objects.all()

	poem = poem_creator(list_of_objects[0], list_of_objects[1])

	return render_to_response('poem_gen/index.html', {'books':list_of_objects}, context_instance=context)

# Create your views here.
