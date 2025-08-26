from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField("Title", max_length=50)
    content = models.TextField("Text")
    counted_views = models.IntegerField("Counted Views", default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(
        default=django.utils.timezone.now, verbose_name="Published Date")
    status = models.BooleanField("Status", default=False)
    # tags = models.ManyToManyField('Tag', related_name='posts')
    # comments = models.ManyToManyField('Comment', related_name='posts')
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-created_date']  # جدیدترین پست‌ها اول

    def __str__(self):
        return self.title


