from django.urls import path
from projectapp import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('sign_in',views.sign_in),
    path('client',views.client),
    path('read_client',views.read_client),
    path('delete_client',views.delete_client),
    path('project',views.project),
    path('read_project',views.read_project)
]