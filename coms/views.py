from functools import partial
from urllib.error import HTTPError
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



from rest_framework.parsers import JSONParser
from coms.models import User, Group, File
from .serializers import UserSerializer, GroupSerializer, FileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from coms import serializers

class UsersView(APIView):

    def get(self,request,format=None):
        """
        Get method to obtain all users in the User table.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

class UserView(APIView):

    def get(self,uid,format=None):
        """
        Get methods to obtain all information on a specific user (based on uid).
        """
        user = User.objects.get(uid=uid)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    def post(self,request,format=None):
        """
        Post methods to create a new user
        """
        input = JSONParser().parse(request)
        serializer = UserSerializer(data = input)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)            

    def put(self,request,uid,format=None):
        """
        Put method to modify a user's information (based on uid).
        """
        input = JSONParser().parse(request)
        user = User.objects.get(uid=uid)
        serializer = UserSerializer(user,data=input,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class GroupsView(APIView):
    
    def get(self,request,format=None):
        """
        Get methods for the group table:
        - Return all groups information from the group table
        """
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return JsonResponse(serializer.data, safe=False) #this line causes an error: 
        #'AssertionError: `HyperlinkedRelatedField` requires the request in the serializer context. 
        #Add `context={'request': request}` when instantiating the serializer'

class GroupView(APIView):
    
    def get(self,request,id,format=None):
        """
        Get method for a particular group (based on group id).
        - Returns all group information
        """
        group = User.objects.get(id=id)
        serializer = UserSerializer(group)
        return JsonResponse(serializer.data)

    def post(self,request,format=None):
        """
        Post methods to create a new group.
        """
        input = JSONParser().parse(request)
        serializer = GroupSerializer(data = input)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        """
        Put method to modify an existing group.
        """
        input = JSONParser().parse(request)
        group = Group.objects.get(id=id)
        serializer = GroupSerializer(group,data=input,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class FileView(APIView):
    
    def get(self,request,format=None):
        pass

    def post(self,request,format=None):
        pass

    def put(self,request,format=None):
        pass
