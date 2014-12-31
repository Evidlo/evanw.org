from django.db import models
from blog.models import *
from sorl.thumbnail import ImageField

# Create your models here.
class Project(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField('project title',max_length=100)
    description = models.TextField('project description')
    text = models.TextField('project text')
    categories = models.ManyToManyField(Category)


def folder_location(instance,filename):
    return instance.project.title+'/'+filename

class Image(models.Model):
    project = models.ForeignKey(Project)
    image = ImageField(upload_to=folder_location)
    description = models.CharField('image description',max_length=200,blank=True)
