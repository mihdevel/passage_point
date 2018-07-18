from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import card

def sensor(request, sensor_id):
  data_cards = card.objects.all()
  
  return render(request, 'passage_point/sensor.html', {'data_cards': data_cards, 'sensor_id': sensor_id})

def sensor_check(request, sensor_id):
  pass