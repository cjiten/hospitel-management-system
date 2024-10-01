# Generated by Django 5.0.4 on 2024-04-25 07:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=255)),
                ('session_id', models.CharField(blank=True, max_length=2555, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
