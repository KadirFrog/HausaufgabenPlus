# Generated by Django 4.2.4 on 2023-08-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haplus', '0011_remove_post_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
    ]
