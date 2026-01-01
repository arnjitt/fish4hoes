from django.db import models

class Event(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  

class Friend(models.Model):
  ENERGY_LEVELS = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High")
  ]
  name = models.CharField(max_length=100)
  energy = models.CharField(
    max_length=10,
    choices=ENERGY_LEVELS,
    default="medium"
  )
  event = models.ForeignKey(
    Event,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="event"
  )

  def __str__(self):
    return self.name
