# Generated by Django 2.1.1 on 2018-11-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0027_remove_qualitycontrol_observation'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='phases',
            field=models.ManyToManyField(through='GestiRED.Phase', to='GestiRED.PhaseType'),
        ),
    ]
