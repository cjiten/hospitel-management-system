# Generated by Django 5.0.4 on 2024-04-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralManagement', '0005_doctormanagement_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormanagement',
            name='fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
