"""photoshare/groups URL Configuration

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



LAST MODIFIED: 2022-11-22 by William Bushie
"""

# imports
from django.urls import path
from .views import CreateGroupView, UserSearchView, CreateSessionView, UpdateSessionView

urlpatterns = [
    path('create/', CreateGroupView.as_view(), name='create_group'),
    path('user/', UserSearchView.as_view(), name='user_search'),
    path('sessions/create/', CreateSessionView.as_view(), name='create_session'),
    path('sessions/update/', UpdateSessionView.as_view(), name='update_session'),
]