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
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30) # this needs to be changed once real password management is implemented
    username = models.CharField(max_length = 30)
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
    users = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    #share_link = models.URLField(max_length=200,default=f'http://127.0.0.1:8000/api/group/{id}/join/',blank=True)
    files = models.ForeignKey(File,blank=True,on_delete=models.CASCADE)
    time_period = models.DurationField(default=timedelta(hours=1))
    creation = models.DateTimeField(default=now,blank=True,editable=False)
    last_updated = models.DateTimeField(auto_now=True,blank=True)
    active = models.BooleanField(default=True,blank=True)

