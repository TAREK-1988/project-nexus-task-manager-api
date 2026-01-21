from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "status", "priority", "assigned_to", "created_at")
    search_fields = ("title", "project__name", "assigned_to__username")
    list_filter = ("status", "priority", "created_at")
