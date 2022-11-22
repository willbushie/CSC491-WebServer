"""photoshare URL Configuration

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

Routers

Helpful Guide: https://medium.com/django-rest/django-rest-framework-creating-views-and-serializers-b76a96fb6fb7
Rest API Docs: https://www.django-rest-framework.org/api-guide/viewsets/



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
from django.contrib import admin
from django.urls import re_path, include
from groups.views import GroupViewSet, UserViewSet, FileViewSet, SessionViewSet, ListViewSet
from rest_framework.routers import DefaultRouter

# creating router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'files', FileViewSet, basename='file')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'list', ListViewSet, basename='list')

# URL patterns
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
]
