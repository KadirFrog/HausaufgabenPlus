# Generated by Django 4.2.4 on 2023-08-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haplus', '0009_alter_post_ersteller'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_teacher',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
    ]
