from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Notes(models.Model):
    anim_name = models.ForeignKey('Anim_name',on_delete=models.CASCADE,)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True,editable=False)
    modifed = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['created',]

    def __str__(self):
        return 'My Note on {}'.format(self.anim_name)



# GODSFAVOUR COMMENTS
# there is still a need to create & edit the animation template 
# to display the notes and a form to add a new note to it

# The model returns an error as 'anim_name' model has't been created yet
# and is linked to the model as a FK