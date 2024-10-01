from django.db import models
from PatientManagement.models import PatientManagement

# Create your models here.

class AppointmentManagement(models.Model):
    fee_mode_stauts = (
    ('online', 'Online'),
    ('offline', 'Offline'),
    ('pending', 'Pending'),
    ('free', 'Free'),
    )

    appointment_id = models.CharField(max_length=50, unique=True)
    patient = models.ForeignKey(PatientManagement, on_delete=models.CASCADE)
    fee = models.IntegerField(null=True, blank=True)
    fee_mode = models.CharField(choices=fee_mode_stauts, max_length=50, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.appointment_id