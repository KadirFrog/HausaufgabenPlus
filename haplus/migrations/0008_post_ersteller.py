# Generated by Django 4.2.4 on 2023-08-09 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haplus', '0007_customuser_can_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ersteller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
