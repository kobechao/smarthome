from django.db import models

# Create your models here.
class RPi_Test_Data(models.Model):
    rPin = models.CharField(max_length=20)
    gPin = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.address