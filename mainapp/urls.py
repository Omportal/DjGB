from django.urls import path
from .views import *


app_name = 'mainapp'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('news', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsPageDetailView.as_view(), name='news_detail'),
    path('doc_site', DocSiteView.as_view(), name='doc_site'),
    path('courses_list', CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:pk>',  CoursesDetailView.as_view(), name='courses_detail'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]