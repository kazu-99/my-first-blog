from django.urls import path
from . import views

app_name = 'f_test'
urlpatterns = [
    path('',views.index,name='index'),
    path('hello',views.hellodjango,name='hello'),
    path('booklist',views.book,name='booklist'),
]
