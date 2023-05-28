from django.contrib import admin
from django.contrib.admin.decorators import register

from issues.models import Issue, Comment
# Register your models here.
@register(Issue)
class Issue(admin.ModelAdmin):
    search_fields = ('issue_name', 'assignee', 'project_linked')
    list_display = ('issue_name', 'assignee', 'priority', 'status')

@register(Comment)
class Comments(admin.ModelAdmin):
    search_fields = ('issue', 'author' , 'text')
    list_display = ('issue', 'text',  'author')