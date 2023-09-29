# Generated by Django 4.2.2 on 2023-07-19 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminuser', '0021_alter_ingredient_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='request', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]