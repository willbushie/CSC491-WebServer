"""
Admin Customization

Helpful Guide: https://medium.com/django-rest/build-a-product-review-backend-with-django-rest-framework-part-2-d86b1c6a08db



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
from django.contrib import admin
from django.contrib.auth.models import Group as auth_group
from django.contrib.auth.models import User
from .models import Group, Session, File, List

# register the Groups Models (created in .models.py)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'admin', 'start')
    list_filter = ('name', 'admin', )

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'group', 'user', 'ip', 'active')
    #list_filter = ('group', 'user', )

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'creator', 'group', 'created')
    #list_filter = ('creator', 'group', )

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'file_id', 'owner')
    #list_filter = ('owner', )

# un-register the default Group Model (used for user permissions and such)
admin.site.unregister(auth_group)

# Modify the Admin Site Title
admin.site.site_header = "Photoshare Admin Site"