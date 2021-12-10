from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.



#class CustomManager(models.Manager):
  #def get_queryset(self):
       #return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (("draft","Draft"),("publish","Publish"),)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    image=models.ImageField(null=True, blank=True, default='/images/')
    publish=models.DateTimeField(default=timezone.now)
    upload_to = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default="draft")
    #objects=CustomManager()
    tags=TaggableManager()


def get_absolute_url(self):
    return reverse('blogapp/post_detail',args=[self.slug])




class Meta:
        ordering = ['-created_on']

def __str__(self):
        return self.title


class Comments(models.Model):
    post=models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class Meta:
    ordering=['-created']

def __str__(self):
    return 'commented by {} on {}'.format(self.name,self.post)
