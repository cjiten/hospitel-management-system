# Generated by Django 5.0.4 on 2024-04-30 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientManagement', '0003_alter_patientmanagement_doctor'),
        ('TreatmentManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatmentmanagement',
            name='appointment',
        ),
        migrations.AddField(
            model_name='treatmentmanagement',
            name='treatment_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='treatmentmanagement',
            name='treatment_patient',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='PatientManagement.patientmanagement'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='treatmentmanagement',
            name='treatment_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
