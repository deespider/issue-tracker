from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from users.models import CustomUser
# Register your models here.
@register(CustomUser)
class CustomUser(admin.ModelAdmin):
    search_fields = ('email', 'name')
    list_display = ('email', 'name')
