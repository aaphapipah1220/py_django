from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.members, name="members"),
    path('members/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name="testing"),
]