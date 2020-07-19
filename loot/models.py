from django.db import models

class Loot(models.Model):
  description = models.CharField(max_length=256)
  quantity = models.PositiveSmallIntegerField()
  est_value = models.PositiveSmallIntegerField(blank=True)
  coin_type = models.CharField(max_length=50, blank=True)
  value_calc = models.CharField(max_length=50, blank=True)
  total_est = models.PositiveSmallIntegerField(blank=True)
  notes = models.TextField(blank=True)
  status = models.CharField(max_length=100, default='unsold')
  actual_value = models.PositiveSmallIntegerField(blank=True)
  
class Coin(models.Model):
  plat = models.PositiveSmallIntegerField()
  gold = models.PositiveSmallIntegerField()
  elec = models.PositiveSmallIntegerField()
  silv = models.PositiveSmallIntegerField()
  copp = models.PositiveSmallIntegerField()
  
  
