from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


# Create your models here.


class Fruits(models.Model):
    PhoneNumber=models.CharField(max_length=12,null= True)
    FullName=models.CharField(max_length=25,null= True)
    FruitName = models.CharField(max_length=100)
    Image = models.ImageField(null=True,blank=True,upload_to="images")
    Price = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)


    def __str__(self):
        return self.FruitName
        #return self.user.username

	
class Course(models.Model):
    title=models.CharField(max_length=25,null= True)
    youtube_link = models.CharField(null= True, blank = True,max_length=100)

    def __str__(self):
        return self.title
         #return self.user.username




class User(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    #phone_number = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)

    profile_pic = models.ImageField(upload_to="profile")


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def _str_(self):
        return self.phone_number   


#picture=models.ImageField(upload_to='pictures/%y/%m/%d/',max_length=255)