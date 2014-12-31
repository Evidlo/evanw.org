from django.contrib import admin
from .models import *

# Register your models here.

class ImageInline(admin.StackedInline):
    model=Image
    extra=4

class ProjectAdmin(admin.ModelAdmin):
    inlines=[ImageInline]

admin.site.register(Project,ProjectAdmin)
