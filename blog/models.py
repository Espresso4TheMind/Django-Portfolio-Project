from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    DISPLAY_CHOICES = [('Public', 'Public'), ('Private', 'Private')]
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    display = models.CharField(choices=DISPLAY_CHOICES, max_length=25)
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=25)
    body = models.TextField(max_length=2500)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['post', '-created_on']

    def __str__(self):
        return self.author
