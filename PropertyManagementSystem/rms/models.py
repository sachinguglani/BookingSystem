from django.db import models

class RoomDetail(models.Model):
  room = models.CharField(max_length=255)
  status = models.CharField(max_length=255)
  startDate = models.DateField(null=True, blank=True)
  endDate = models.DateField(null=True, blank=True)

  def __str__(self):
        return self.room + self.status 