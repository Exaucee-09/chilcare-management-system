# Generated by Django 5.1.2 on 2024-10-24 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0003_alter_child_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2005, 1, 1)),
        ),
    ]