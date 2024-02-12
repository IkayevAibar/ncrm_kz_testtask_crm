from django.contrib.auth.models import Group, User

from rest_framework import permissions, viewsets, filters
from django_filters import rest_framework as django_filters

from .models import Board, Status, Task, TaskHistory
from .serializers import UserSerializer, BoardSerializer, StatusSerializer, TaskSerializer, TaskHistorySerializer

class TaskFilter(django_filters.FilterSet):
    min_due_date = django_filters.DateFilter(field_name='due_date', lookup_expr='gte')
    max_due_date = django_filters.DateFilter(field_name='due_date', lookup_expr='lte')
    priority = django_filters.NumberFilter(field_name='priority')
    status = django_filters.CharFilter(field_name='status__name')

    class Meta:
        model = Task
        fields = ['min_due_date', 'max_due_date', 'priority', 'status']


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.AllowAny]  

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.AllowAny]  

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TaskFilter
    ordering_fields = ['due_date', 'priority']

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.assigned_to:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Вы не можете изменить статус этой задачи.")



class TaskHistoryViewSet(viewsets.ModelViewSet):
    queryset = TaskHistory.objects.all()
    serializer_class = TaskHistorySerializer
    permission_classes = [permissions.AllowAny]  
