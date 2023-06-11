from django.contrib import admin
from django.contrib.admin.decorators import register

from projects.models import Project
# Register your models here.
@register(Project)
class Project(admin.ModelAdmin):
    search_fields = ('project_name', 'project_link')
    list_display = ('project_name', 'project_link')
