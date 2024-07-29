# Generated by Django 5.0.6 on 2024-06-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beta', models.FloatField(default=0.1)),
                ('start', models.IntegerField(default=2000)),
                ('end', models.IntegerField(default=2100)),
                ('dt', models.FloatField(default=1.0)),
            ],
        ),
    ]
