from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('news', NewsView.as_view(), name='news'),
    path('doc_site', DocSiteView.as_view(), name='doc_site'),
    path('courses_list', CoursesListView.as_view(), name='courses_list'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]