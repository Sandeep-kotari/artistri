from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.





    


class User(AbstractUser):
    is_User = models.BooleanField('is_user', default=False)
    is_admin = models.BooleanField('is_admin', default=False)
    # is_staff = models.BooleanField('is_staff', default=False)
    profile_photo=models.ImageField(upload_to='profile/',default=settings.STATIC_URL + 'images/default.png')
    bio=models.CharField(max_length=200,default='',null=True)
    
    

    def save(self, *args, **kwargs):
        if self.is_superuser and not self.is_admin:
            self.is_admin = True
            self.is_staff=True
        super().save(*args, **kwargs)



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

class like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    number_of_like=models.BigIntegerField()

class article(models.Model):
    title = models.CharField(max_length=200,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_article', blank=True)

    # def __str__(self):
    #     return self.title
