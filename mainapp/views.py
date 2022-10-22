from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import News, Courses, Lesson, CourseTeachers


class MainView(TemplateView):
    template_name: str = 'index.html'


class NewsView(ListView):
    model = News
    template_name: str = 'news.html'
    def get_queryset(self):
        return super().get_queryset().all()

class NewsPageDetailView(TemplateView):
    template_name = "news_detail.html"
    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(News, pk=pk)
        return context

class ContactsView(TemplateView):
    template_name: str = 'contacts.html'


class CoursesListView(TemplateView):
    template_name: str = 'courses_list.html'
    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = Courses.objects.all()[:7]
        return context

class CoursesDetailView(TemplateView):
    template_name: str = "courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(Courses, pk=pk)
        context["lessons"] = Lesson.objects.filter(
        course=context["course_object"]
        )
        context["teachers"] = CourseTeachers.objects.filter(
        course=context["course_object"]
        )
        return context
class DocSiteView(TemplateView):
    template_name: str = 'doc_site.html'


class LoginView(TemplateView):
    template_name: str = 'login.html'
