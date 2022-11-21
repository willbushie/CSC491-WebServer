"""
Groups Models
Database models for groups. 

Helpful Guide: https://medium.com/django-rest/lets-build-a-basic-product-review-backend-with-drf-part-1-652dd9b95485



LAST MODIFIED: 2022-11-21 by William Bushie
"""

# imports
from django.db import models
from django.contrib.auth.models import User



class Group(models.Model):
    """
    ### Groups
    Groups are started when members want to share file during an event/period of time.
    - name (CharField): The admin entered name for the event
    - active (BooleanField): If the group is currently active (i.e. the event is still going).
    - duration (DurationField): The entered (or updated) duration of the event.
    - start (DateField): Time and date of the start of the event.
    - end (DateField): Time and date of the end of the event.
    - admin (ForeignKey): The user ID who started (or is currently heading) the event.
    - join_link (URLField): The link which can be used to join this event (only active durring the event).

    Note: (group) ID is an included field.

    ### Future
    - [5] "end" needs to be modified to find the difference between start & duration.
    - [5] "join_link" needs to be auto-generated.
    - [5] "admin" can be changed if the previous admin leaves the share group.
    - [1] "name" should allow emojis to be entered in the name of the group.
    """
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    duration = models.DurationField(default=1)
    # start is set for when the group is started
    start = models.DateField(auto_now=True)
    # end is set by finding (start + duration)
    end = models.DateField(auto_now=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    join_link = models.URLField(default="http://www.photoshare.com/group/join/788") # this needs to be auto generated in some fasion

    def __str__(self):
        return self.name

class Session(models.Model):
    """
    ### Sessions
    Sessions are used to keep track of which users are in which groups
    - group (ForeignKey): ID of the group in which the user is participating. 
    - user (ForeignKey): ID of the user participating in the group.

    Note: (session) ID is an included field.
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class File(models.Model):
    """
    ### Files
    Files is used to keep track of all files that are to be shared within groups.
    - creator (ForeignKey): ID of the user who created the file.
    - group (ForeignKey): ID of the group in which the file should be shared.
    - created (DateField): Date and time of when the file was created.
    - size (): Size of the file to be shared (not currently used).

    Note: (file) ID is an included field. 
    Note: "size" is not a currently used field.

    ### Future
    - [5] Obtain the "created" value from the user application when a file is shared.
    - [2] Find the size of a file to help in time to download calculation.
    """
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # obtained through the application
    created = models.DateField(default="2022-12-31")
    #size = models.

class List(models.Model):
    """
    ### List
    List contains all files that each user owns. Used for sharing lookup.
    - file_id (ForeignKey): ID of file that is owned by user.
    - owner (ForeignKey): ID of user that owns the file.

    Note: (list) ID is an included field.
    """
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)