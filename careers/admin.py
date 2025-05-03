from django.contrib import admin
from .models import JobOpening

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = (
        'position', 'type', 'location', 'department', 'formatted_posted_date', 'short_description',
    )
    list_filter = ('type', 'department', 'location', 'posted')
    search_fields = ('position', 'location', 'department', 'description', 'requirements')
    date_hierarchy = 'posted'
    ordering = ('-posted',)

    fieldsets = (
        ('Job Info', {
            'fields': ('position', 'type', 'location', 'department', 'posted')
        }),
        ('Job Details', {
            'fields': ('description', 'requirements')
        }),
    )

    def formatted_posted_date(self, obj):
        return obj.posted.strftime('%b %d, %Y')  # e.g., "Nov 15, 2023"
    formatted_posted_date.short_description = 'Posted On'

    def short_description(self, obj):
        return (obj.description[:75] + '...') if len(obj.description) > 75 else obj.description
    short_description.short_description = 'Description Preview'
