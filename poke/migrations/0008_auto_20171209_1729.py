# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0007_auto_20171209_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compare',
            name='First',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='First', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='compare',
            name='Second',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Second', to='poke.Pokemon'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Pokemons',
            field=models.ManyToManyField(to='poke.Pokemon'),
        ),
    ]
