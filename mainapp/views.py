from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name: str = 'index.html'


class NewsView(TemplateView):
    template_name: str = 'news.html'
    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={'range': range(5)})

class NewsWithPaginatorView(NewsView):
    
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context

class ContactsView(TemplateView):
    template_name: str = 'contacts.html'


class CoursesListView(TemplateView):
    template_name: str = 'courses_list.html'


class DocSiteView(TemplateView):
    template_name: str = 'doc_site.html'


class LoginView(TemplateView):
    template_name: str = 'login.html'
