from django.db import models
import os
from poem_maker import settings

def get_file_path(instance, filename):
	return os.path.join('texts', filename)

class TextInput(models.Model):
	get_file_path = os.path.join(settings.MEDIA_ROOT, 'texts')
	name = models.CharField(max_length = 200, blank=False)
	author = models.CharField(max_length = 200, blank=True)
	text = models.FileField(upload_to=get_file_path,blank=False)
	# text = models.FileField(upload_to="texts")
	def __unicode__(self):
		
		return self.name
