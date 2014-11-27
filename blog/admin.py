from django.contrib import admin
from blog.models import Post,Category,NavLink

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ['pub_date','categories']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(NavLink)
