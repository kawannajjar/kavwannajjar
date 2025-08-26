from django.contrib import admin

from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',
                    'subject', 'short_message',
                    'created_date', 'updated_date',
                    ]
    search_fields = ('name', 'email')
    list_filter = ('created_date', 'updated_date')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = "Message"


admin.site.register(Contact, ContactAdmin)
# Register your models here.
