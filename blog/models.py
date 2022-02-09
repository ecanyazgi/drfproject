from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import NewUser
from django.utils import timezone
from . import enums
from . managers import PostQuerySet

class Category(models.Model):
    name = models.CharField(max_length=100)
     
    
    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(
        Category,on_delete=models.PROTECT,default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank = True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name = 'blog_posts') 
    status = models.CharField(max_length=10,choices=enums.Options.choices,default=enums.Options.PUBLISHED)
    objects = models.Manager()
    postobjects = PostQuerySet.as_manager()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title




