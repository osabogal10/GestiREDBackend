# Generated by Django 2.1.1 on 2018-10-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0005_auto_20181004_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fase',
            name='fechaFinal',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]