# Generated by Django 3.0.8 on 2020-07-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('est_value', models.PositiveSmallIntegerField()),
                ('uom', models.CharField(max_length=100)),
                ('total_est', models.PositiveSmallIntegerField()),
                ('notes', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('actual_value', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
