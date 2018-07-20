from django.db import models
from django.utils import timezone

class card(models.Model):
  """docstring for card"""
  id = models.CharField(primary_key=True, max_length=10)
  
  def __str__(self):
    return self.id
  

class card_cross(models.Model):
  """docstring for card_cross"""
  id = models.AutoField(primary_key=True)
  check_detetime = models.DateTimeField(default=timezone.now)
  card_id = models.ForeignKey('card', on_delete=models.CASCADE)
  sensor = models.CharField(max_length=6)
  
  def __str__(self):
    return self.sensor