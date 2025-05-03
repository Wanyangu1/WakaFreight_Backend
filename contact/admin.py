from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'short_message', 'created_at')
    list_filter = ('created_at', 'service')
    search_fields = ('name', 'email', 'phone', 'message', 'service')
    readonly_fields = ('name', 'email', 'phone', 'service', 'message', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'service')
        }),
        ('Message Content', {
            'classes': ('collapse',),
            'fields': ('message',),
        }),
        ('Metadata', {
            'fields': ('created_at',),
        }),
    )

    def short_message(self, obj):
        return (obj.message[:50] + '...') if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message Preview'
