# Generated by Django 4.2.4 on 2023-08-09 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haplus', '0008_post_ersteller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ersteller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]