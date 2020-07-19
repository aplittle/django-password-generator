# Generated by Django 3.0.8 on 2020-07-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loot', '0003_auto_20200714_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loot',
            name='uom',
        ),
        migrations.AddField(
            model_name='loot',
            name='coin_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='loot',
            name='value_calc',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='loot',
            name='actual_value',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='loot',
            name='est_value',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='loot',
            name='status',
            field=models.CharField(default='unsold', max_length=100),
        ),
        migrations.AlterField(
            model_name='loot',
            name='total_est',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]