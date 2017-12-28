# Generated by Django 2.0 on 2017-12-28 13:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0022_auto_20171228_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='Appearance',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='Picture',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='gender_type',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='region_type',
        ),
        migrations.AlterField(
            model_name='compare',
            name='CompareTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 28, 16, 12, 19, 912957)),
        ),
        migrations.AlterField(
            model_name='compare',
            name='First',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='First', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='compare',
            name='Second',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Second', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Pokemons',
            field=models.ManyToManyField(to='poke.Pokemon'),
        ),
    ]
