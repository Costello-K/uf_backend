from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from task.models import Task

from .serializers import TaskSerializer

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for Task objects, providing CRUD operations for task management.

    Attributes:
        serializer_class (class): The serializer class used for task object serialization.
        permission_classes (list): The list of permission classes applied to the viewset.
        ordering (tuple): The default ordering for the queryset results.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering = ('created_at', )

    def get_queryset(self):
        """
        Get the list of tasks for the current user.

        Returns:
            queryset (QuerySet): The filtered queryset containing tasks created by the current user.
        """
        queryset = Task.objects.filter(author=self.request.user)

        queryset = queryset.order_by(*self.ordering)

        return queryset
