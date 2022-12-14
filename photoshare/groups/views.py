"""
ViewSets (class based views) for Groups

Helpful Guide: https://medium.com/django-rest/django-rest-framework-creating-views-and-serializers-b76a96fb6fb7
Rest API Docs: https://www.django-rest-framework.org/api-guide/viewsets/


LAST MODIFIED: 2022-11-22 by William Bushie
"""

# imports
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import GroupSerializer, UserSerializer, FileSerializer, SessionSerializer, ListSerializer, CreateGroupSerializer, CreateSessionSerializer, UpdateSessionSerializer
from .models import Group, User, File, Session, List
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import UpdateModelMixin

class GroupViewSet(viewsets.ViewSet):
    """
    ### Group ViewSet
    Actions: 
    - list (GET): Obtains all groups from the database.
    - retrieve (GET): Obtains a specified group (based on pk) from the database.
    """
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Group.objects.all()
        group = get_object_or_404(queryset, pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

class UserViewSet(viewsets.ViewSet):
    """
    ### User ViewSet
    Actions: 
    - list (GET): Obtains all users from the database.
    - retrieve (GET): Obtains a specified user (based on pk) from the database.

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
class FileViewSet(viewsets.ViewSet):
    """
    ### File ViewSet
    Actions: 
    - list (GET): Obtains all users from the database.
    - retrieve (GET): Obtains a specified user (based on pk) from the database.

    """
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = File.objects.all()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = File.objects.all()
        file = get_object_or_404(queryset, pk=pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)

class SessionViewSet(viewsets.ViewSet):
    """
    ### Session ViewSet
    Actions: 
    - list (GET): Obtains all sessions from the database.
    - retrieve (GET): Obtains a specified session (based on pk) from the database.

    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'group']
    permission_classes = [IsAuthenticated]


    def list(self, request):
        queryset = Session.objects.all()
        serializer = SessionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Queries the database and obtains sessions based on group id.
        """
        queryset = Session.objects.all()
        session = get_object_or_404(queryset, pk=pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

class ListViewSet(viewsets.ViewSet):
    """
    ### List ViewSet
    Actions: 
    - list (GET): Obtains all list items from the database.
    - retrieve (GET): Obtains a specified list item (based on pk) from the database.

    """
    serializer_class = ListSerializer
    queryset = List.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = List.objects.all()
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = List.objects.all()
        list = get_object_or_404(queryset, pk=pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)

class CreateGroupView(generics.CreateAPIView):
    """
    ### Create Group View

    """
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = CreateGroupSerializer

class CreateSessionView(generics.CreateAPIView):
    """
    ### Create Session View

    """
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = CreateSessionSerializer

class UserSearchView(generics.RetrieveAPIView):
    """
    ### User Search View
    Actions: 
    - retrieve (GET): Obtains a specified group (based on pk) from the database.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    
    def retrieve(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class PartialUpdateSessionView(generics.GenericAPIView, UpdateModelMixin):
    ""
    ### Update Session View

    ""
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = UpdateSessionSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SessionListSearch(generics.ListAPIView):
    # Search the sessions given group id (user is )
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        user = self.request.user
        group = self.kwargs['group']
        return Session.objects.filter(user=user,group=group)
