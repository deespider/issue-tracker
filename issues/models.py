from django.db import models
from users.models import CustomUser
from projects.models import Project

# Create your models here.
class Issue(models.Model):
    PRIORITIES = (
        (1, "Low"),
        (2, "Medium"),
        (3, "High")
    )
    STATUSES = (
        (1, "ToDo"),
        (2, "InProgress"),
        (3, "Done"),
        (4, "Blocked")
    )
    issue_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    assignee = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, related_name='assigned_issues')
    priority = models.SmallIntegerField(choices=PRIORITIES, default=1)
    project_linked = models.ForeignKey(to=Project,on_delete=models.PROTECT, related_name='linked_project')
    status =models.SmallIntegerField(choices=STATUSES, default=1)

    def __str__(self):
        return self.issue_name
    
class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    # Additional fields and methods as needed

    def __str__(self):
        return self.text[:50]
