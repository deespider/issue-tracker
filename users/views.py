from django.shortcuts import render
from requests import Request
from rest_framework.views import APIView
from projects.serializers import ProjectAddSerializer
from rest_framework.response import Response
from rest_framework import status as drf_response_status
from users.serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)
