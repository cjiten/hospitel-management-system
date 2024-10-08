# Generated by Django 5.0.4 on 2024-04-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreatmentManagement', '0006_alter_treatmentmanagement_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentmanagement',
            name='treatment_deposit_mode',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline'), ('pending', 'Pending'), ('free', 'Free')], default=('pending', 'Pending'), max_length=50),
        ),
        migrations.AlterField(
            model_name='treatmentmanagement',
            name='treatment_stauts',
            field=models.CharField(choices=[('started', 'Started'), ('pending', 'Pending'), ('ended', 'Ended')], default=('pending', 'Pending'), max_length=50),
        ),
    ]
