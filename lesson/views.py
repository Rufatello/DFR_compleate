from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated,AllowAny
from lesson.models import Course, Lesson, Payments, Subscribe
from lesson.paginations import LessonPagination
from lesson.serliazers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscribeSerializer
from users.permissions import IsModerator, IsUser


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated | IsModerator | IsUser]
    pagination_class = LessonPagination

    def get_queryset(self):
        if self.request.user.role == "member":
            return Course.objects.filter(user=self.request.user)
        elif self.request.user.role == 'moderator':
            return Course.objects.all()

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsModerator]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsUser]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated | IsUser | IsModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsModerator, IsUser]
        return [permission() for permission in permission_classes]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator, IsUser]
    permission_classes = [AllowAny]
    pagination_class = LessonPagination

    # def get_queryset(self):
    #     if self.request.user.role == "member":
    #         return Lesson.objects.filter(user=self.request.user)
    #     elif self.request.user.role == 'moderator':
    #         return Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated, IsModerator, IsUser]
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     new_lesson = serializer.save()
    #     new_lesson.user = self.request.user
    #     new_lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsModerator]


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('data_payments',)
    filterset_fields = ('paid_course', 'payment_method',)


class SubscribeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsUser]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()
