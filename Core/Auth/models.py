from django.db import models
import uuid

# Create your models here.

class AuthUser(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, primary_key=True)
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=255)
    session_id = models.CharField(max_length=2555, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name