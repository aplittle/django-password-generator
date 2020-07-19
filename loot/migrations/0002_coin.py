# Generated by Django 3.0.8 on 2020-07-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat', models.PositiveSmallIntegerField()),
                ('gold', models.PositiveSmallIntegerField()),
                ('elec', models.PositiveSmallIntegerField()),
                ('silv', models.PositiveSmallIntegerField()),
                ('copp', models.PositiveSmallIntegerField()),
            ],
        ),
    ]