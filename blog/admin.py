from django.contrib import admin
from blog.models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
