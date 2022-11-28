"""
Serializers for Groups

Helpful Guide: https://medium.com/django-rest/django-rest-framework-creating-views-and-serializers-b76a96fb6fb7



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
from django.contrib.auth.models import User
from .models import Group, Session, File, List
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    """
    ### User Serializer
    """
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    """
    ### Group Serializer
    Inlcudes: 
    - pk
    - name
    - active
    - duration
    - start
    - end
    - admin
    - join_link
    """
    class Meta:
        model = Group
        fields = ['pk', 'name', 'active', 'duration', 'start', 'end', 'admin', 'join_link']

class SessionSerializer(serializers.ModelSerializer):
    """
    ### Session Serializer
    Includes: 
    - pk
    - group
    - user
    """
    class Meta:
        model = Session
        fields = ['pk', 'group', 'user']

class FileSerializer(serializers.ModelSerializer):
    """
    ### File Serializer
    Includes: 
    - pk
    - creator
    - group
    - created
    """
    class Meta:
        model = File
        fields = ['pk', 'creator', 'group', 'created']

class ListSerializer(serializers.ModelSerializer):
    """
    ### List Serializer
    Includes:
    - pk
    - file_id
    - owner
    """
    class Meta:
        model = List
        fields = ['pk', 'file_id', 'owner']

class CreateGroupSerializer(serializers.ModelSerializer):
    """
    ### Group Creation Serializer

    """

    start = serializers.DateTimeField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    class Meta:
        model = Group
        fields = ('name', 'active', 'duration', 'start', 'end', 'admin', 'join_link')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        """
        Create a group event.
        """
        group = Group.objects.create(
            name=validated_data[''],
            active=validated_data[''],
            duration=validated_data[''],
            #end=validated_data[''],
            admin=validated_data[''],
            #join_link=validated_data['']
        )

        group.save()
        return group

class JoinGroupSerializer(serializers.ModelSerializer):
    """
    
    """
    pass