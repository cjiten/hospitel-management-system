# Generated by Django 5.0.4 on 2024-04-30 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreatmentManagement', '0005_alter_treatmentmanagement_treatment_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentmanagement',
            name='treatment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
