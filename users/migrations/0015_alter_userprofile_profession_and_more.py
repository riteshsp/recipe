# Generated by Django 4.2.2 on 2023-08-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_userprofile_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='static/profilepic'),
        ),
    ]
