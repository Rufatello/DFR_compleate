from django.contrib import admin

from lesson.models import Lesson, Course


@admin.register(Lesson)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Course)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)