# Generated by Django 4.0.6 on 2022-07-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
