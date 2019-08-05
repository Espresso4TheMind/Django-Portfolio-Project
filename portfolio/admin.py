from django.contrib import admin
from portfolio.models import Project, Technology


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display', 'project_status', 'start_date', 'finish_date')
    list_filter = ('display',)
    fields = [
        'display',
        'title',
        'description',
        ('project_status', 'start_date', 'finish_date'),
        'github_link',
        'tech'
    ]


class TechnologyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
