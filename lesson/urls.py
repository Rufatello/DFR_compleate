from django.urls import path
from rest_framework.routers import DefaultRouter
from lesson.apps import LessonConfig
from lesson.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView

app_name = LessonConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
]+router.urls