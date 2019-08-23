from django.shortcuts import render
from blog.models import Post
from portfolio.models import Project
from django.core.exceptions import ObjectDoesNotExist


def homepage(request):
    page_title = 'Home'
    try:
        latest_post = Post.objects.exclude(display='Private').latest('created_on')
    except ObjectDoesNotExist:
        latest_post = None
    try:
        latest_project = Project.objects.exclude(display='Private').latest('start_date')
    except ObjectDoesNotExist:
        latest_project = None
    context = {
        'page_title': page_title,
        'post': latest_post,
        'project': latest_project,
    }
    return render(request, 'homepage.html', context)


def about(request):
    page_title = 'Biography'
    context = {
        'page_title': page_title
    }
    return render(request, 'about.html', context)


def contact(request):
    page_title = 'Contact Info'
    context = {
        'page_title': page_title
    }
    return render(request, 'contact.html', context)


def events(request):
    page_title = 'Events'
    context = {
        'page_title': page_title
    }
    return render(request, 'fullcalendar_base.html', context)
