# Generated by Django 3.0.3 on 2020-02-22 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='when_to_play',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
