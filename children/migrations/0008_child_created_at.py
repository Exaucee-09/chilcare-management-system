# Generated by Django 5.1.2 on 2024-11-18 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0007_remove_child_parent_guardian_child_parent_guardian'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
