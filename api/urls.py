from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, TestView

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('<int:pk>/', include(router.urls)),
  path('builtin-json/', TestView.as_view()),
  ]