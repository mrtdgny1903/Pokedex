# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0002_auto_20171209_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compare',
            name='First',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='First', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Picture',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Pokemons',
            field=models.ManyToManyField(to='poke.Pokemon'),
        ),
    ]
