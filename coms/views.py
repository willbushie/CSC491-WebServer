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


""" @api_view(['GET'])
def api_overview(request):
    client_get_urls = {
        'List of grouped members':'/api/groups/<int:id>/members/',
        'List of members current IPs':'/api/groups/<int:id>/ips/',
        'List of shareables files':'/api/groups/<int:id>/files/',
        'Group member current IP':'/api/groups/<int:id>/members/<int:uid>/ip/',
        'Group member files list':'/api/groups/<int:id>/members/<int:uid>/files/',
    }

    client_post_urls = {
        'New shareable file':'/api/groups/<int:id>/newfile/',
        'IP address change':'/api/groups/<int:id>/ipupdate/',
        'New group creation':'/api/groups/new/'
    }

    return JsonResponse({'GET':client_get_urls,'POST':client_post_urls}) """

class UsersView(APIView):

    def get(self,request,format=None):
        """
        Get methods for the users table:
        - Return all users information from user table
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

class UserView(APIView):

    def get(self,request,uid,format=None):
        """
        Get methods for the user table:
        - Return all user info given the user uid
        """
        user = User.objects.get(uid=uid)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    def post(self,request,action='create',uid=None,format=None):
        """
        Post methods to the user table:
        - create: create a new user in the database
        - update_ip: update a user's last_known_ip & last_seen values
        - deactivate: update a user's deactivate & last_seen values
        """
        input = JSONParser().parse(request)
        if action != 'create':
            user = User.objects.get(uid=uid)

        # udpate user last_known_ip & last_seen values
        if action == 'update_ip':
            serializer = UserSerializer(user,data=input,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        # update user _deactivated & last_seen values
        elif action == 'deactivate':
            serializer = UserSerializer(user,data=input,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        # create new user in the database (all feilds required, else an error occurs)
        elif action == 'create':
            serializer = UserSerializer(data = input)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        # produce an error
        else:
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
        pass

    def post(self,request,id,action='create',format=None):
        """
        Post methods for the group table:
        - create: create a new group
        - 
        """
        input = JSONParser().parse(request)
        if action != 'create':
            group = Group.objects.get(id=id)

        # udpate group users w/new user & last_updated values
        if action == 'add_user':
            serializer = GroupSerializer(group,data=input,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            


        # udpate group files w/new file & last_updated values
        if action == 'new_file':
            serializer = GroupSerializer(group,data=input,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        # update group time_period & last_updated values
        if action =='update_time_period':
            serializer = GroupSerializer(group,data=input,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        # udpate group active & last_updated values
        elif action == 'deactivate':
            serializer = GroupSerializer(group,data=input,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        # create new group in the database (all feilds required, else an error occurs)
        elif action == 'create':
            serializer = GroupSerializer(data = input)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        # produce an error
        else:
            return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class FileView(APIView):
    
    def get(self,request,format=None):
        pass

    def post(self,request,format=None):
        pass
