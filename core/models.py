from django.db import models
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(upload_to = "profile_images",default = 'noPhoto.jpg')
    location = models.CharField(max_length=30,blank=True)
    firstName = models.CharField(max_length=20,default = " ")
    lastName  = models.CharField(max_length=20,default= " ")
    
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()

    def __str__(self):
        return self.user
