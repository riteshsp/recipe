# Generated by Django 4.2.2 on 2023-06-28 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0007_rename_calculated_rating_id_recipe_calculated_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='recipedescription_ingredient',
            old_name='Ingredient',
            new_name='ingredient',
        ),
    ]
