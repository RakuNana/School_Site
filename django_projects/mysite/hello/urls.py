from django.urls import path

from . import views

app_name = 'Hello'

urlpatterns = [
    path('', views.hello_view, name='hello'),
]