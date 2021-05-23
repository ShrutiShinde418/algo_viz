from .models import *
from .serializers import *
from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,redirect
from django.urls import path



# Create your views here.
class AccountListCreate(generics.ListCreateAPIView):
    queryset=AccountUser.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=AccountSerializer

# class ReactView(APIView):
#     serializer_class = ReactSerializer

#     def get(self, request):
#         detail = [{"name": detail.name, "detail": detail.detail}
#                   for detail in AccountUser.objects.all()]
#         return Response(detail)

#     def post(self, request):
#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     def redirect_view(self,request):
#         Response=redirect('http://localhost:3000')
#         return Response


