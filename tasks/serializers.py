from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "project",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "assigned_to",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
