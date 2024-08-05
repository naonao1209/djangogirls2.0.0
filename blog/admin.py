from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'image', 'created_date', 'status')
    search_fields = ('title', 'text', 'status')
    list_filter = ('created_date', 'published_date')

admin.site.register(Post, PostAdmin)