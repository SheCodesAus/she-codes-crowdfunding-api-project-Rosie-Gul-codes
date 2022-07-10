from django.contrib.auth import get_user_model
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner_projects')

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='pledges')
    supporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='supporter_pledges')
    

#If owner & supporter is not specified, they will be inhereted from the user_id. 
#user_id includes username, email address & the authentication token.
#The authentication token identifies who the user is automatically.