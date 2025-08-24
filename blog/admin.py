from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'counted_views',
                    'created_date', 'updated_date',
                    'published_date', 'status')
    search_fields = ('title', 'content')
    list_filter = ('created_date', 'updated_date', 'published_date', 'status')
    date_hierarchy = 'created_date'


admin.site.register(Post, PostAdmin)

# Register your models here.
