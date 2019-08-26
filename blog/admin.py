from django.contrib import admin
from blog.models import Post, Comment, Blogger
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Blogger)


"""@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass"""

class BloggerInline(admin.StackedInline):
    model = Blogger
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (BloggerInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date')
    list_filter = ('post_date', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = 'post_date', 'commenter', 'corresponding_post'
    list_filter = ('commenter', 'post_date', 'corresponding_post')
    fields = ('corresponding_post', 'content', ('post_date', 'commenter'))




