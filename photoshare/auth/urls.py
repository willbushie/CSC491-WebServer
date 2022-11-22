"""photoshare/auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

===============================================================================

URLs & Routers

Helpful Guide (Views & Serializers): https://medium.com/django-rest/django-rest-framework-creating-views-and-serializers-b76a96fb6fb7
Helpful Guide (JWT): https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8
Rest API Docs (ViewSets): https://www.django-rest-framework.org/api-guide/viewsets/
Rest API Docs (Routers): https://www.django-rest-framework.org/api-guide/routers/



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
from django.urls import path
from auth.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
]
