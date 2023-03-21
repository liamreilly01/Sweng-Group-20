from django.urls import path
from . import views

urlpatterns = [
    path('database/', views.database, name='database'),
    path('legislationList/', views.legislationList, name="legislationList"),
    path('legislationList/<str:key>', views.legislationDetail, name="legislation")
]