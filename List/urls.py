from django.urls import path

from .views import *

app_name = 'list'

urlpatterns = [
    path('', HomeView.as_view(), name='list')
]