# Generated by Django 2.1.1 on 2018-10-26 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0017_auto_20181026_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.EventType'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='phaseType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.PhaseType'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resourceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestiRED.ResourceType'),
        ),
    ]
