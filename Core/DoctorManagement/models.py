from django.db import models

# Create your models here.

class DoctorManagement(models.Model):
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fee = models.IntegerField(default=0, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name