from django.urls import path
from . import views

urlpatterns = [
    path('', views.acts, name='acts'),
    # cpath('details/<int:id>', views.details, name='details'),
]