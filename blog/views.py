from django.template import RequestContext,loader
from django.http import HttpResponse
from blog.models import Post, Category

# Create your views here.
def index(request,category=None):

	if category:
		posts = Category.objects.get(title=category).post_set.all()
	else:
		posts = Post.objects.all()

	template = loader.get_template('blog/index.html')
	context = RequestContext(request,{
		'posts':posts,
	})

	return HttpResponse(template.render(context))
