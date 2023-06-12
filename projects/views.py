from django.shortcuts import render
from requests import Request
from rest_framework.views import APIView
from projects.serializers import ProjectAddSerializer
from rest_framework.response import Response
from rest_framework import status as drf_response_status

class ManageProjectsAPI(APIView):

    def post(self, request):
        status = drf_response_status.HTTP_200_OK
        message = "Project Saved"
        name = request.data.get("poject_name")
        descriptions = request.data.get("project_descriptions")
        url =  request.data.get("project_url")
        project_data = {
            "project_name": name,
            "project_description": descriptions,
            "project_link" : url
        }
        project_serializer = ProjectAddSerializer(data=project_data)
        try:
            if project_serializer.is_valid(raise_exception=True):
                project_serializer.save()
        except Exception as e:
            status = drf_response_status.HTTP_400_BAD_REQUEST
            message = f"Project not saved as:{str(e)}"
        
        return Response(status=status, data={"status": status, "message": message, "data":{}})

