from django.contrib import admin
from blogapp.models import Post,Comments

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','image',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body','created','updated','active')
    list_filter = ('active','created','updated')
    search_fields = ['name', 'email','body']

admin.site.register(Comments,CommentAdmin)
