# Generated by Django 2.1.1 on 2018-10-07 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0008_merge_20181006_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fase',
            name='resource',
        ),
        migrations.AddField(
            model_name='resource',
            name='fases',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GestiRED.Fase'),
            preserve_default=False,
        ),
    ]
