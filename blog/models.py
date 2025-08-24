from django.db import models

class Post(models.Model):
    # image
    # authot
    title = models.CharField((""), max_length=50)
    content = models.TextField((""))
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) # 2025-08-24 21:24:01.854947
    published_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    