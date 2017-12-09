# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompareTime', models.DateField()),
                ('SpecialName', models.CharField(max_length=120)),
                ('First', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='poke.Pokemon')),
            ],
        ),
        migrations.AddField(
            model_name='trainer',
            name='Pokemons',
            field=models.ManyToManyField(to='poke.Pokemon'),
        ),
    ]
