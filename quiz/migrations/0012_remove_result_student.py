# Generated by Django 3.0.8 on 2021-09-19 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20210919_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='student',
        ),
    ]