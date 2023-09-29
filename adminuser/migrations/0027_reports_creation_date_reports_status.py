# Generated by Django 4.2.2 on 2023-07-21 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0026_rename_my_date_field_request_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reports',
            name='status',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]