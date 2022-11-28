"""
Views for Auth



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
import traceback
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework import generics

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

class LogoutView(APIView):
    """
    Logout a user & blacklist the JWTs.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            #traceback.print_exc()
            return Response(status=status.HTTP_400_BAD_REQUEST)

