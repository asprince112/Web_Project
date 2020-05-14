from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    
    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Article', related_name='comments', on_delete = models.CASCADE)
    author = models.CharField(max_length=120)
    text = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    
    def get_absolute_url(self):
        return reverse("blog:article_list")

    def __str__(self):
        return self.text