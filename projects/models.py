from django.db import models

# Create your models here.
class Project(models.Model):
	def __unicode__(self):
		return self.title

	title = models.CharField('project title',max_length=100)
	text = models.TextField('project text')
	thumbnail = models.ImageField

