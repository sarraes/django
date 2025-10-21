from django.contrib import admin
from .models import Conference, Session 
from datetime import datetime, date, timedelta 

admin.site.site_title = "Gestion Conférence 25/26"
admin.site.site_header = "Gestion Conférence"
admin.site.index_title = "Django App Conférence"

@admin.register(Session)
class AdminSessionModel(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "conference",
        "session_day",
        "start_time",
        "end_time",
        "room",
        "duration_minutes", 
    )
    
    ordering = ("session_day", "start_time")
    list_filter = ("topic",)
    search_fields = ("title", "topic", "room", "conference__name")
    date_hierarchy = "session_day"
    readonly_fields = ("session_id", "created_at", "update_at")

    fieldsets = (
        ("Détails de la Session", {
            "fields": ("session_id", "conference", "title", "topic")
        }),
        ("Planification et Lieu", {
            "fields": ("session_day", "start_time", "end_time", "room")
        }),
        ("Horodatages", {
            "fields": ("created_at", "update_at"),
            "classes": ("collapse",)
        }),
    )

    def duration_minutes(self, obj):
        if obj.start_time and obj.end_time:
            start_minute = obj.start_time.hour * 60 + obj.start_time.minute
            end_minute = obj.end_time.hour * 60 + obj.end_time.minute
            total_minute =abs( end_minute - start_minute )
            hours = total_minute // 60
            minutes = total_minute % 60
        
            return f"{hours}h {minutes:02d}m"
    
         
