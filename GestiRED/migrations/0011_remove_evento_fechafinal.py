# Generated by Django 2.1.1 on 2018-10-07 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestiRED', '0010_auto_20181007_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='fechaFinal',
        ),
    ]
