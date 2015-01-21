from django.shortcuts import render, render_to_response
from django.template import RequestContext
from poem_gen.models import TextInput
from poem_maker import settings
# from poem_creator import poem_creator
import re
import nltk
from random import randint
import logging 
import time 
import os

nltk.data.path.append('./nltk_data/')

def poem_creator(object1, object2):
	# print(object1.name, object2.name)
	# object1.text.open()
	# object2.text.open()
	# text1 = object1.text.readlines()
	# text2 = object2.text.readlines()
	# print(text1[0:10], text2[0:10])

	final_poem = str()
	first = str()
	second = str()
	object1.text.open()
	line_list1 = object1.text.readlines()
	for line in line_list1:
		first += line
	first = first.strip().replace('\r',' ').replace('\n', ' ')
	first = first.split(' ')
	first = filter(None, first)
	# first = re.split('\W+', first)
	# first = [x.split(' ') for x in first.split('\n')]
	object2.text.open()
	line_list2 = object2.text.readlines()
	for line in line_list2:
		second += line
	second = second.strip().replace('\r',' ').replace('\n', ' ')
	second = second.split(' ')
	second = filter(None, second)
	# second = re.split('\W+', second)
	# second = [x.split(' ') for x in second.split('\n')]

	conj = ['CC', 'IN', 'DT']
	verbs = ['VBZ', 'VBG', 'VBD', 'VBN', 'VBP']
	nouns = ['NN', 'NNS']
	sets = [conj, verbs, nouns]

	books = [first, second]
	whichbook = 0
	whichword = randint(0, len(first))
	currentbook = books[whichbook]
	currentword = currentbook[whichword]


	for x in xrange(0, 8):
		i = 0

		#selects a random point in the text and then finds the beginning of a sentence
		while True:
			currentword = currentbook[whichword]
			if '.' in currentword:
				whichword+=1
				break
			else:
				whichword+=1

		while True:
			currentbook = books[whichbook]
			currentword = currentbook[whichword]

			if '.' in currentword:
				final_poem += currentword + " " 
				# output.write(currentword + " ")
				break

			if i > 1:
				while True:
					if '.' in currentword:
						final_poem += currentword + " "
						# output.write(currentword + " ")
						break
					else:
						final_poem += currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " " 
						# output.write(currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " ")
						whichword+=1
						currentword = currentbook[whichword]
				break

			# text = unicode(nltk.word_tokenize(currentword),errors='ignore')
			text = nltk.word_tokenize(currentword)
			text = nltk.pos_tag(text)

			for g, group in enumerate(books):
				# Ignore the same list
				if group == currentbook:
					continue

				# If the currentWord is in a different list:
				if text[0][1] in verbs:
					# switch lists to the new list
					whichbook = g
					i+=1
					#output.write('\n')
					try:
						# switch word index to word
						whichword = group.index(currentword, randint(0, len(group))) 
					except:
						whichword = group.index("and", randint(0, len(group)-100))
			
			final_poem += currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " " 
			# output.write(currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " ")
			whichword+=1
		final_poem += '\n'
		# output.write('\n')
	final_poem += '\n'
	# output.write('\n')
	return final_poem

def index(request):
	logging.basicConfig(filename = 'views.log', level = logging.INFO)
	logging.info('Started: {} {}'.format(time.strftime("%H:%M:%S"), time.strftime("%d/%m/%Y")))

	context = RequestContext(request)

	list_of_objects = TextInput.objects.all()
	try:
		poem = poem_creator(list_of_objects[0], list_of_objects[1])
	except (IndexError, IOError) as e:
		list_of_objects = []
		poem = "No poem!"
		logging.exception(e)
		files_in_text = os.listdir("{}/{}".format(settings.MEDIA_ROOT,"texts"))
		logging.info(files_in_text)

	return render_to_response('poem_gen/index.html', {'books':list_of_objects, 'poem':poem}, context_instance=context)

# Create your views here.
