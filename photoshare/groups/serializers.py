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
    - ip
    - active
    """
    class Meta:
        model = Session
        fields = ['pk', 'group', 'user', 'ip', 'active']

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

    """ start = serializers.DateTimeField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            ) """

    class Meta:
        model = Group
        fields = ('id', 'name', 'active', 'duration', 'start', 'end', 'admin', 'join_link')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        """
        Create a group event.
        """
        group = Group.objects.create(
            name=validated_data['name'],
            #active=validated_data[''],
            #duration=validated_data[''],
            #start=validated_data[''],
            #end=validated_data[''],
            admin=validated_data['admin'],
            join_link="",
        )
        # this link is not used in the android application
        group.join_link = f"http://www.photoshare.com/groups/{group.pk}/"
        group.save()
        return group

class CreateSessionSerializer(serializers.ModelSerializer):
    """
    ### Session Creation Serializer

    """

    class Meta:
        model = Session
        fields = ('id', 'group', 'user', 'ip', 'active')

    def create(self, validated_data):
        """
        Create a Session event.
        """
        session = Session.objects.create(
            group=validated_data['group'],
            user=validated_data['user'],
            ip=validated_data['ip'],
            active=validated_data['active'],
        )
        session.save()
        return session

class UpdateSessionSerializer(serializers.ModelSerializer):
    """
    ### Session Update Serializer

    """

    class Meta:
        model = Session
        fields = ('ip', 'active')

    def update(self, validated_data):
        """
        Update a Session with a new active value.
        """
        session = Session.objects.update(
            active=validated_data['active'],
            ip=validated_data['ip']
        )
        return session
