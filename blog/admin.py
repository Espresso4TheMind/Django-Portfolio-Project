from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display', 'created_on', 'last_modified')
    list_filter = ('tags',)


class TagAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on')
    list_filter = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
