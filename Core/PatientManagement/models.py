from django.db import models
from DoctorManagement.models import DoctorManagement
from datetime import date

# Create your models here.

class PatientManagement(models.Model):
    sex_name = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    )

    full_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True, blank=True)
    care_of = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    sex = models.CharField(choices=sex_name, max_length=50, null=True, blank=True)
    aadhar = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    doctor = models.ForeignKey(DoctorManagement, on_delete=models.DO_NOTHING, null=True, blank=True)
    remark = models.CharField(max_length=500, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f'/patient/{self.pk}/'

    @property
    def age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age