# service_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),             # http://127.0.0.1:8000/service/
    path('heavy_task/', views.heavy_task, name='heavy_task'), # http://127.0.0.1:8000/service/heavy_task/
]