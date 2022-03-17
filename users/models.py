from tkinter import Image
import uuid
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from setuptools import Require
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    desc = models.TextField(max_length=250,blank=True)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)