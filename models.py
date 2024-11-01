
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title
