from rest_framework import serializers
from .models import User, File, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'uid',
            'email',
            'password',
            'username',
            'account_creation',
            'last_seen',
            'last_known_ip',
            'active',
        ]
        
        # rename instance to that of the uid
        def __str__(self):
            return self.uid

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = [
            'id',
            #'metadata',
            'time',
            'author',
        ]

        # rename instance to that of the id
        def __str__(self):
            return self.id


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'users',
            #'share_link',
            'files',
            'time_period',
            'creation',
            'last_updated',
            'active',
        ]

        # rename instance to that of the id
        def __str__(self):
            return self.id

