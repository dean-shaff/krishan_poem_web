from django.db import models


class TextInput(models.Model):
	name = models.CharField(max_length = 200, blank=False)
	author = models.CharField(max_length = 200, blank=True)
	text = models.FileField(upload_to ='texts',blank=False)

	def __unicode__(self):
		
		return self.name
