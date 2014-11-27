from django.shortcuts import render
from django.template import RequestContext, loader
from django.templatetags.static import static
from django.http import HttpResponse,HttpResponseRedirect,Http404
import os
from evanw_org import settings

# Create your views here.
def downloads(request,location):
	basedir = settings.filelist['BASEDIR']
	path = basedir+location

	if os.path.isdir(basedir + location):
		#get directory listing
		os.chdir(basedir + location)
		raw_items = os.listdir('.')
		items = [{'name':item,'isdir':os.path.isdir(item),'size':os.path.getsize(item)/1000000} for item in raw_items]
		items.sort()
		vars = {
		'basedir':basedir,
		'location':location,
		'items':items,
		}

		template = loader.get_template('downloads/downloads.html')
		context = RequestContext(request, vars)
		#return render(request,'downloads/downloads.html',vars)
		return HttpResponse(template.render(context))
	elif os.path.isfile(basedir + location):
		print location
		return HttpResponseRedirect(static('downloads/test.html'))
	else:
		vars = {
		'error':'Could not find location "{0}" in BASEDIR "{1}"'.format(location,basedir),
		}
		template = loader.get_template('404.html')
		context = RequestContext(request,vars)
		return HttpResponse(template.render(context))
