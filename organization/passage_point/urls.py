from django.urls import path
from . import views

app_name = 'passage_point'
urlpatterns = [
    path('sensor/<str:sensor_id>/pass/', views.sensor, name='sensor'),
    path('sensor/<str:sensor_id>/check/', views.sensor_check, name='sensor_check'),
    path('check_pass', views.check_pass, name='check_pass'),
    path('check_pass_return', views.check_pass_return, name='check_pass_return'),
    
]