from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, date
from .models import card, card_cross


def sensor(request, sensor_id):
  data_cards = card.objects.all()
  return render(request, 'passage_point/sensor.html', {'data_cards': data_cards, 'sensor_id': sensor_id})
  # return HttpResponse(data_cards)


def sensor_check(request, sensor_id):
  enter_card_id = request.POST['card_id']
  card_id = card.objects.get(id=enter_card_id)

  new_card_cross = card_cross(
    check_detetime = timezone.now(),
    card_id = card_id,
    sensor = sensor_id
  )
  new_card_cross.save()
  
  return HttpResponseRedirect(reverse('passage_point:sensor', args=(sensor_id,)))


def check_pass(request):
  return render(request, 'passage_point/calculation.html',)


def check_pass_return(request):
  date_start = request.POST['date_start']
  date_finish = request.POST['date_finish']
  
  # Не смог полученные дату перевести в datetime объекты, сделал так
  date_start = date_start.split('-')
  date_finish = date_finish.split('-')
  
  datetime_start_object = datetime(int(date_start[0]), int(date_start[1]), int(date_start[2], 10))
  datetime_finish_object = datetime(int(date_finish[0]), int(date_finish[1]), int(date_finish[2], 10))
  
  data_pass_input = card_cross.objects.filter(check_detetime__gte=datetime_start_object).filter(check_detetime__lte=datetime_finish_object).filter(sensor='input')
  data_pass_output = card_cross.objects.filter(check_detetime__gte=datetime_start_object).filter(check_detetime__lte=datetime_finish_object).filter(sensor='output')

  count_pass = dict(input=data_pass_input.count(), output=data_pass_output.count())
  
  return render(request, 'passage_point/result.html', {'count_pass': count_pass})
  # return HttpResponse(data_pass_output.count())