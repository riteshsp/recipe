# Generated by Django 4.2.2 on 2023-07-25 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminuser', '0027_reports_creation_date_reports_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=3500)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='adminuser.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
