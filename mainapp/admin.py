from django.contrib import admin
from .models import News, Lesson
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", 'description_as_markdown']
    ordering = ["-course__name", "-num"]
    list_per_page: int = 5
    list_filter = ["course", "created", 'description_as_markdown']
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    def mark_deleted(self, request, queryset):
        queryset.update(description_as_markdown=True)

    mark_deleted.short_description = "Mark deleted"
    get_course_name.short_description = "Course"