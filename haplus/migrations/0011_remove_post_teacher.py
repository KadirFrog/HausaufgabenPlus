# Generated by Django 4.2.4 on 2023-08-09 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haplus', '0010_customuser_is_teacher_post_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='teacher',
        ),
    ]