from django import forms
from django.contrib import admin
from blog.models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'published_date': forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'counted_views', 'created_date',
                    'updated_date', 'published_date', 'status')
    search_fields = ('title', 'content')
    list_filter = ('created_date', 'updated_date', 'published_date', 'status')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'

    def save_model(self, request, obj, form, change):
        if not obj.published_date:
            obj.published_date = timezone.now()
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
