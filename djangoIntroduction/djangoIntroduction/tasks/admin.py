from django.contrib import admin

from djangoIntroduction.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_filter = ('title',)
    ordering = ('-title',)
