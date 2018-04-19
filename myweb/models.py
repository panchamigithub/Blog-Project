from django.db import models

# Create your models here.


class register(models.Model):
   username=models.CharField(max_length=100,unique=True)
   name=models.CharField(max_length=100)
   email=models.EmailField(max_length=255)
   mobile=models.CharField(max_length=100)
   password=models.CharField(max_length=100)
   city=models.CharField(max_length=100)
   ans=models.CharField(max_length=100,default="")

   def __str__(self):
     return '%s %s'%(self.username,self.password)

class blog(models.Model):
   #uname=models.ForeignKey('register',on_delete=models.CASCADE,)
   blogp=models.CharField(max_length=255,default="")
   author=models.CharField(max_length=100,default="")
   username=models.CharField(max_length=100,default="")
   title=models.CharField(max_length=100,default="")

class comments(models.Model):
   post_id=models.CharField('Post')
   comment=models.CharField(max_length=225)
