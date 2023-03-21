from django.urls import path
from . import views

urlpatterns = [
    path('database/', views.database, name='database'),
]