from django.contrib.auth import get_user_model
from rest_framework import serializers

from task.models import Task
from user.serializers import UserSerializer

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer class for Task objects.
    """
    author = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new Task object.

        Args:
            validated_data (dict): The validated data from the serialized request.
        Returns:
            Task: The newly created Task object.
        """
        # add an authorized user as an author
        validated_data['author'] = self.context['request'].user

        # create a new task
        task = Task.objects.create(**validated_data)

        return task
