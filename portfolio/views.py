from django.shortcuts import render
from portfolio.models import Project


def portfolio_index(request):
    page_title = 'Programming Portfolio'
    projects = Project.objects.exclude(display='Private').order_by('project_status', '-start_date')
    context = {
        'projects': projects,
        'page_title': page_title,
    }
    return render(request, 'portfolio_index.html', context)


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'page_title': project.title,
        'finish_date': project.finish_date,
    }
    return render(request, 'project_details.html', context)


def project_technology(request, tech):
    projects = Project.objects.filter(tech__name__contains=tech).exclude(display='Private').order_by('-start_date')
    context = {
        'tech': tech,
        'projects': projects,
        'page_title': tech,
    }
    return render(request, 'portfolio_index.html', context)
