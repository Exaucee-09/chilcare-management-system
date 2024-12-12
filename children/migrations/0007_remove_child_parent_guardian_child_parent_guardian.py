# Generated by Django 5.1.2 on 2024-11-18 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0006_alter_child_gender'),
        ('parents', '0002_alter_parentguardian_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='parent_guardian',
        ),
        migrations.AddField(
            model_name='child',
            name='parent_guardian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='parents.parentguardian'),
        ),
    ]