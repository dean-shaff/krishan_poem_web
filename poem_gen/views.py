from django.shortcuts import render, render_to_response
from django.template import RequestContext
from poem_gen.models import TextInput
from poem_maker import settings
from poem_gen.forms import PoemGenUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files import File

# from poem_creator import poem_creator
import re
import nltk
from random import randint
import logging 
import time 
import os

nltk.data.path.append('./nltk_data/')
text_dir = os.path.join(settings.MEDIA_ROOT,'texts')
# text_dir = 'texts'

# books = {"Heart of Darkness by Joseph Conrad":fileconrad,
#         "The Metamorphosis by Frank Kafka":filekafka,
#         "A Collection of Chinese Fairy Tales":filechina,
#         "A Collection of Persian Fairy Tales":filefairy,
#         "The Yellow Wallpaper by Charlotte Gilman Perkins":fileyellow,
#         "A Manual about the History of Steam Power":filesteam,
#         "Dead Men Tell No Takes by E. W. Hornung": filedeadmen,
#         "A Treatise of the History of Glass by Edward Dillon":fileglass,
#         "A Take of Two Cities by Charles Dickens":filedickens,
#         "A Critique of Pure Reason by Immanuel Kant":filekant }

def poem_creator(object1, object2):
	# print(object1.name, object2.name)
	# object1.text.open()
	# object2.text.open()
	# text1 = object1.text.readlines()
	# text2 = object2.text.readlines()
	# print(text1[0:10], text2[0:10])

	final_poem = str()
	if isinstance(object1, TextInput) and isinstance(object2, TextInput):	
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

	elif isinstance(object1, str) and isinstance(object2, str):
		first = open(os.path.join(text_dir,object1)).read().strip().replace('\r',' ').replace('\n', ' ')
		first = first.split(' ')
		first = filter(None, first)

		second = open(os.path.join(text_dir,object2)).read().strip().replace('\r',' ').replace('\n', ' ')
		second = second.split(' ')
		second = filter(None, second)

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
	files_in_text = os.listdir("{}/{}".format(settings.MEDIA_ROOT,"texts"))
	list_of_objects = TextInput.objects.all()

	# available_files = []
	# for file_name in files_in_text:
	# 	for object in list_of_objects:
	# 		if file_name.strip(".txt") in str(object.text.path):
	# 			available_files.append(file_name)
	# print(available_files)
	# try:
	# 	poem = poem_creator(available_files[0], available_files[1])
	# except (IndexError, IOError) as e:
	# 	list_of_objects = []
	# 	poem = "No poem!"
	# 	logging.exception(e)
	# 	files_in_text = os.listdir("{}/{}".format(settings.MEDIA_ROOT,"texts"))
	# 	logging.info(files_in_text)
	getted = []
	poem = str()
	try:
		if request.method == "GET":
			request_dict = dict(request.GET)
			print(request_dict)
			for id_num in request_dict.values():
				if id_num[0] == '':
					pass
				elif id_num[0] != '':
					print
					getted.append(TextInput.objects.get(id=str(id_num[0])))
		else:
			pass

		if len(getted) == 2:
			poem = poem_creator(getted[0], getted[1])
			# poem = poem1.replace(u'\n','<br />')
			# poem = cgi.escape(poem)
		elif len(getted) < 2:
			poem = "Not enough texts selected to generate a poem. Pick two and try again!"

	except (IOError, IndexError) as err:
		poem = "Error -- no poem generated"
		logging.exception(err)

	return render_to_response('poem_gen/index.html', {'books':list_of_objects, 'poem':poem, 'getted':getted}, context_instance=context)

def upload_book(request):
	logging.basicConfig(filename = 'views.log', level = logging.INFO)
	logging.info('Started: {} {}'.format(time.strftime("%H:%M:%S"), time.strftime("%d/%m/%Y")))
	context = RequestContext(request)

	try: 
		if request.method == "POST":
			# below is how i would do this with the django form. Have this set up, just don't want to use it.
			# print(request.FILES)
			# book_form = PoemGenUploadForm(request.POST, request.FILES)

			# if book_form.is_valid():
			# 	book_form.save()
			# else:
			# 	logging.info(book_form.errors)
				# print(book_form.errors)

			request_dict = dict(request.POST)
			file_dict = dict(request.FILES)
			try:
				title = request_dict['title'][0]
				author = request_dict['author'][0]
				text_file = file_dict['file_to_upload'][0]
				with open(os.path.join(text_dir, text_file.name),'w') as writer:
					for chunk in text_file.chunks():
						writer.write(chunk)

				new_book = TextInput()
				new_book.name = str(title)
				new_book.author = str(author)
				new_book.text = os.path.join(text_dir, text_file.name)
				new_book.save()
				return HttpResponseRedirect('/')
			except (KeyError, IOError) as err1:
				print(err1)
				logging.exception(err1)

			
	except (IOError, IndexError) as err:
		logging.exception(err)

	return render_to_response('poem_gen/upload.html', {}, context_instance=context)

	# return HttpResponseRedirect('/upload/')