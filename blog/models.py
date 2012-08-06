from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 200)
    url = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    def __unicode__(self):
        return self.title