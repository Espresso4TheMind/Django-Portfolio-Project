from django.db import models
# import os
# from django.conf import settings


class Technology(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

    def __str__(self):
        return self.name


class Project(models.Model):
    DISPLAY_CHOICES = [('Public', 'Public'), ('Private', 'Private'),]
    PROJECT_STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
        ('Indefinite', 'Indefinite'),
    ]
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    display = models.CharField(choices=DISPLAY_CHOICES, max_length=25)
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_status = models.CharField(choices=PROJECT_STATUS_CHOICES, max_length=25)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    github_link = models.URLField()
    tech = models.ManyToManyField('Technology')
    # image = models.FilePathField(path='./img/icons')
    # image = models.FilePathField(path=os.path.join('portfolio', 'static', 'img'))

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ['-start_date', '-created_on']

    def __str__(self):
        return self.title
