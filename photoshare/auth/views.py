"""
Views for Auth



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ChangePasswordSerializer, CustomTokenObtainPairSerializer, UpdateUserSerializer
from rest_framework import generics

class CustomObtainTokenPairView(TokenObtainPairView):
    """
    Override of the ObtainTokenPairView from simpleJWT.
    """
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    """
    Register a user and save the user.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    """
    Update a user's password.
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):
    """
    Update portions of a user's profile.
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
