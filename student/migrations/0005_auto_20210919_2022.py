# Generated by Django 3.0.8 on 2021-09-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210919_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
