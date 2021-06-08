from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_images/',null = True)

class Room(models.Model):
    room_id = models.CharField(max_length=10)
    room_admin = models.ForeignKey(User,on_delete=models.CASCADE)

class Chat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    text = models.TextField(max_length=1500,null=True,blank=True)
    file = models.FileField(upload_to='audio')

