from django.contrib import admin

from apps.tasks_planning.models import Task, TaskCategory


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'bot_user', 'category', 'countable_value', 'date', 'done']
    list_filter = ['date', 'done', 'category']
    search_fields = ['task_name', 'category', 'date']


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
