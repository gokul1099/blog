from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField('date published', auto_now_add=True,null=True)
    image_link = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return self.title + " | " + str(self.author)
