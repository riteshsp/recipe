# Generated by Django 4.2.2 on 2023-06-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]