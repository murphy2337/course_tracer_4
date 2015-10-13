from django.db import models

# Create your models here.


class CSDept(models.Model): 
	title = models.CharField(max_length=512)
	content = models.TextField()

	def __unicode__(self):
		return self.title

class UniversityInformationSystems(models.Model): 
	title = models.CharField(max_length=512)
	content = models.TextField()

	def __unicode__(self):
		return self.title

class Data(models.Model): 
	title = models.CharField(max_length=512)
	content = models.TextField()

	def __unicode__(self):
		return self.title

class Report(models.Model): 
	title = models.CharField(max_length=512)
	content = models.TextField()

	def __unicode__(self):
		return self.title
