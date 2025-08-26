from django.db import models

class Post(models.Model):
    title = models.CharField("Title", max_length=50)
    content = models.TextField("Text")
    counted_views = models.IntegerField("Counted Views", default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)      
    published_date = models.DateTimeField("Published Date")
    status = models.BooleanField("Status", default=False)

    class Meta:
        ordering = ['-created_date']  # جدیدترین پست‌ها اول

    def __str__(self):
        return self.title
