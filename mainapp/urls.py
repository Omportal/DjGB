from django.urls import path
from .views import *


app_name = 'mainapp'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('news', NewsListView.as_view(), name='news'),
    path("news/create/", NewsCreateView.as_view(), name="news_create"),
    path('news/<int:pk>/detail', NewsDetailView.as_view(), name='news_detail'),
    path("news/<int:pk>/update", NewsUpdateView.as_view(), name="news_update",),
    path("news/<int:pk>/delete", NewsDeleteView.as_view(), name="news_delete",),

    path('doc_site', DocSiteView.as_view(), name='doc_site'),

    path('courses_list', CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:pk>',  CoursesDetailView.as_view(), name='courses_detail'),
    path("course_feedback/", CourseFeedbackFormProcessView.as_view(), name="course_feedback",),

    path('contacts', ContactsView.as_view(), name='contacts'),
]