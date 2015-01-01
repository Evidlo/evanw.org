from django.db import models
from blog.models import *
from sorl.thumbnail import ImageField

# Create your models here.
class Project(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField('title',max_length=100)
    description = models.TextField('short description')
    text = models.TextField('description')
    categories = models.ManyToManyField(Category)
    pub_date = models.DateField('publish date')
    status = models.CharField('status',max_length=16)

    def status_color(self):
        colors = {'Complete':'green','Incomplete':'red','On Hiatus':'yellow'}
        if self.status in colors.keys():
            return colors[self.status]
        else:
            return ''


def folder_location(instance,filename):
    return instance.project.title+'/'+filename

class Image(models.Model):
    project = models.ForeignKey(Project)
    image = ImageField(upload_to=folder_location)
    description = models.CharField('image description',max_length=200,blank=True)
