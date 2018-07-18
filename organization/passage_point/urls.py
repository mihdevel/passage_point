from django.urls import path

from . import views

urlpatterns = [
    path('sensor/<str:sensor_id>/pass/', views.sensor, name='sensor'),
    path('sensor/<str:sensor_id>/check/', views.sensor_check, name='sensor_check'),
]