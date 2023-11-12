# myapp/urls.py
from django.urls import path
from .views import listen_view, TodoListView

urlpatterns = [
    path('listen/', listen_view, name='listen'),
    path('todos/', TodoListView.as_view(), name='todo_list'),
]
