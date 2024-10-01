from django.db import models
from PatientManagement.models import PatientManagement

# Create your models here.

class TreatmentPlan(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class TreatmentManagement(models.Model):
    treatment_stauts_step = [
    ('started', 'Started'),
    ('pending', 'Pending'),
    ('ended', 'Ended'),
    ]
    treatment_deposit_mode_stauts = [
    ('online', 'Online'),
    ('offline', 'Offline'),
    ('pending', 'Pending'),
    ('free', 'Free'),
    ]

    treatment_id = models.CharField(max_length=50, unique=True)
    treatment_name = models.CharField(max_length=1000, null=True, blank=True)
    treatment_cost = models.IntegerField(null=True, blank=True, default='0')
    treatment = models.TextField(null=True, blank=True)
    treatment_patient = models.ForeignKey(PatientManagement, on_delete=models.CASCADE)
    treatment_stauts = models.CharField(choices=treatment_stauts_step, max_length=50, default='Pending')
    treatment_deposit = models.IntegerField(null=True, blank=True, default='0')
    treatment_deposit_mode = models.CharField(choices=treatment_deposit_mode_stauts, max_length=50, default='Pending')
    created_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.treatment_id