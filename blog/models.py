from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


    def approval(self):
          return self.comments.filter(approved = True)

    def get_absolute_url(self):
        return reverse("blogpost_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    blogpost = models.ForeignKey('blog.BlogPost', related_name = 'comments',  on_delete = models.CASCADE)
    author = models.CharField(max_length = 128)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default = False)

    def approval(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('blogpost_list')

    def __str__(self):
        return self.text
