from django.shortcuts import render
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
# models
from core.models import User

# Serializers
from core.serializers import UserSerializer
# Create your views here.
   
#---------
# User |
#---------

class UserList(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=False, methods=['GET','POST'])
    def get(self,request):
        print(request)
        snippet = User.objects.all()
        serializer = self.serializer_class(snippet,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    serializerClass = UserSerializer
    @action(detail=True, methods=['get','put','delete'])
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self, request,  format=None):
        snippet = self.get_object(request.query_params.get('id'))
        serializer = self.serializerClass(snippet)
        return Response(serializer.data)

    def put(self, request,  format=None):
        snippet = self.get_object(request.query_params.get('id'))
        serializer = self.serializerClass(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,  format=None):
        snippet = self.get_object(request.query_params.get('id'))
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

  
#---------
# School |
#---------

# class SchoolList(APIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
#     @action(detail=False, methods=['GET','POST'])
#     def get(self,request):
#         print(request)
#         snippet = School.objects.all()
#         serializer = self.serializer_class(snippet,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer= SchoolSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

# class SchoolDetails(APIView):
#     serializerClass = SchoolSerializer
#     @action(detail=True, methods=['get','put','delete'])
#     def get_object(self, pk):
#         try:
#             return School.objects.get(pk=pk)
#         except School.DoesNotExist:
#             raise Http404
#     def get(self, request,  format=None):
#         snippet = self.get_object(request.query_params.get('id'))
#         serializer = self.serializerClass(snippet)
#         return Response(serializer.data)

#     def put(self, request,  format=None):
#         snippet = self.get_object(request.query_params.get('id'))
#         serializer = self.serializerClass(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,  format=None):
#         snippet = self.get_object(request.query_params.get('id'))
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
