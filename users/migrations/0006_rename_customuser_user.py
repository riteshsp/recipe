# Generated by Django 4.2.2 on 2023-06-20 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0005_rename_user_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]