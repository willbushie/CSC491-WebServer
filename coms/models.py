import uuid
from django.utils.timezone import now
from django.db import models
from datetime import timedelta



class User(models.Model):
    """
    All user information accessed here.
    """

    # fields
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 30) # this needs to be changed once real password management is implemented
    account_creation = models.DateTimeField(default=now,blank=True,editable=False)
    last_seen = models.DateTimeField(auto_now=True,blank=True)
    last_known_ip = models.GenericIPAddressField()
    active = models.BooleanField(default=True,blank=True)

class File(models.Model):
    """
    All shareable file infromation accessed here.
    """

    # fields
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    #metadata =  # metadata resrouce: https://en.wikipedia.org/wiki/Exif
    time = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

class Group(models.Model):
    """
    All shareable group creation accessed here.
    """

    # fields
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    users = models.ManyToManyField(User)
    share_link = models.URLField(max_length=200,default=f'http://127.0.0.1:8000/api/group/{id}/join/')
    files = models.ManyToManyField(File,blank=True)
    time_period = models.DurationField(default=timedelta(hours=1))
    creation = models.DateTimeField(default=now,blank=True,editable=False)
    last_updated = models.DateTimeField(auto_now=True,blank=True)
    active = models.BooleanField(default=True,blank=True)

