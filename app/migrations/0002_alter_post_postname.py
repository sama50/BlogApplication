# Generated by Django 3.2.12 on 2022-09-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postname',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
