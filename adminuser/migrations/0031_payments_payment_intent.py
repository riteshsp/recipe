# Generated by Django 4.2.2 on 2023-07-31 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0030_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_intent',
            field=models.CharField(default='NA', max_length=3500),
            preserve_default=False,
        ),
    ]
