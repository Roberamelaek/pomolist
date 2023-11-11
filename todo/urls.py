# myapp/urls.py
from django.urls import path
from .views import listen_view

urlpatterns = [
    path('listen/', listen_view, name='listen'),
]
