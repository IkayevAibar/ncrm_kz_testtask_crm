from django.contrib.auth.models import Group, User

from rest_framework import serializers

from .models import Board, Status, Task, TaskHistory

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TaskHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskHistory
        fields = "__all__"
