from django.contrib import admin
from .models import User, Group, File

# Register your models here.
admin.site.register(User)
admin.site.register(Group)
admin.site.register(File)