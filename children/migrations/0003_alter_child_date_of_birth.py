# Generated by Django 5.1.2 on 2024-10-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0002_delete_testmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='date_of_birth',
            field=models.DateField(default='01-01-2000'),
        ),
    ]
