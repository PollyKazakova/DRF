from django.db import models

# Create your models here.
class Post(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=40)
    content = models.TextField()
