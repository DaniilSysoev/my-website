from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('hellos', views.hellos, name='hellos'),
    path('create-hello', views.create_hello, name='create-hello')
]
