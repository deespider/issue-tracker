from django.urls import include, path
from projects.views import ManageProjectsAPI
urlpatterns = [
    path('add', ManageProjectsAPI.as_view())
]
