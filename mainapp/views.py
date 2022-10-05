from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name: str = 'index.html'


class NewsView(TemplateView):
    template_name: str = 'news.html'


class ContactsView(TemplateView):
    template_name: str = 'contacts.html'


class CoursesListView(TemplateView):
    template_name: str = 'courses_list.html'


class DocSiteView(TemplateView):
    template_name: str = 'doc_site.html'


class LoginView(TemplateView):
    template_name: str = 'login.html'
