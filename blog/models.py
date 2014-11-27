from django.db import models

# Create your models here.
class Post(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField('post title',max_length=100)
    text = models.TextField('post text')
    pub_date = models.DateTimeField('publish date')
    categories = models.ManyToManyField('blog.Category')

class Category(models.Model):
    def __unicode__(self):
		return self.title

    title = models.CharField('category name',max_length=100)

class NavLink(models.Model):
    def __unicode__(self):
        return self.url

    title = models.CharField('link title',max_length=100)
    url = models.CharField('link URL',max_length=200)

