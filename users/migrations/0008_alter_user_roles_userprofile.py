# Generated by Django 4.2.2 on 2023-06-20 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_roles_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.roles'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=255)),
                ('profilePic', models.ImageField(upload_to='recipe/images')),
                ('verification_code', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]