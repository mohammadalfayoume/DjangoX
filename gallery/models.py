from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.

class Gallery(models.Model):
    title= models.CharField(max_length=50)
    img_url= models.TextField()
    purchaser= models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description= models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery_list')