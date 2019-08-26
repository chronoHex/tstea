# Generated by Django 2.2.4 on 2019-08-14 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20190813_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='user_name',
        ),
        migrations.AddField(
            model_name='blogger',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
