from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from coms import views

urlpatterns = [
    #path('',views.api_overview,name="api_overview"),
    path('users/',views.UsersView.as_view()),
    
    path('user/create/',views.UserView.as_view()),
    path('user/<str:uid>/',views.UserView.as_view()),
    path('user/<str:uid>/<str:action>/',views.UserView.as_view()),
    path('groups/',views.GroupsView.as_view()),
    path('group/create/',views.GroupView.as_view()),
    path('group/<int:id>/join/',views.GroupView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)