from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    designation = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
