from django.db import models
import os

def get_file_path(instance, filename):
	return os.path.join('texts', filename)

class TextInput(models.Model):
	name = models.CharField(max_length = 200, blank=False)
	author = models.CharField(max_length = 200, blank=True)
	text = models.FileField(upload_to=get_file_path,blank=False)

	def __unicode__(self):
		
		return self.name
