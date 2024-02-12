from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'tasks-history', views.TaskHistoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls