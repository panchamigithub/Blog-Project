from django.db import models

# Create your models here.

class Blog_Post(models.Model):
   blogpost = models.CharField(max_length=255)
   author = models.CharField(max_length=100)
   username = models.CharField(max_length=100)

   class Meta:
        verbose_name = "Blog_Post"
        verbose_name_plural = "Blog_Posts"

   def __unicode__(self):
        return '%s %s' % (self.username, self.author)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)