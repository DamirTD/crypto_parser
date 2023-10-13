from django.urls import path
from . import views

urlpatterns = [
    path('cryptocurrency/', views.get_cryptocurrency_info, name='get_cryptocurrency_info'),
]