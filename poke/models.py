from django.db import models
import datetime
class Pokemon(models.Model):

    Name = models.CharField(max_length=40)
    Picture =models.CharField(max_length=120)
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Abilities =models.CharField(max_length=40)
    Deff = models.IntegerField()
    Attack = models.IntegerField()
    Speed = models.IntegerField()
    Appearence = models.CharField(max_length=120)
    
    Type = (
        ('0', 'Fire'),
        ('1', 'Water'),
        ('2', 'Poison'),
        ('3', 'Grass'),
        ('4', 'Bug'),
        ('5', 'Electric'),
        ('6', 'Ice'),
        ('7', 'Fairy'),
        ('8', 'Ground'),
        ('9', 'Dark'),
        ('10', 'Psychic'),
        ('11', 'Fighting'),
        ('12', 'Steel'),
        ('13', 'Ghost'),
        ('14', 'Dragon'),
        ('15', 'Flying'),
    )
    skill_type = models.CharField(max_length=1, choices=Type)



    Gender = (
        ('0', 'Male'),
        ('1', 'Female'),

    )
    gender_type = models.CharField(max_length=1, choices=Gender)

    Generation = (
        ('0', 'I'),
        ('1', 'II'),
        ('2', 'III'),
        ('3', 'IV'),
        ('4', 'V'),
        ('5', 'VI'),
        ('6', 'VII'),

    )
    generation_type = models.CharField(max_length=1, choices=Generation)

class Trainer(models.Model):

    Name = models.CharField(max_length=40)
    Picture =models.CharField(max_length=120)
    Appearance = models.CharField(max_length=120)
    Pokemons = models.ManyToManyField(Pokemon)
    Gender = (
        ('0', 'Male'),
        ('1', 'Female'),

    )
    gender_type = models.CharField(max_length=1, choices=Gender)

    Region = (
        ('0', 'Kanto'),
        ('1', 'Johto'),
        ('2', 'Hoenn'),
        ('3', 'Sinnoh'),
        ('4', 'Unova'),
        ('5', 'Kalos'),
        ('6', 'Alola'),

    )
    region_type = models.CharField(max_length=1, choices=Region)

class Compare(models.Model):
    First = models.ForeignKey(Pokemon,on_delete=models.CASCADE())
    Second = models.ForeignKey(Pokemon,on_delete=models.CASCADE())
    CompareTime = models.DateField()
    SpecialName = models.CharField(max_length=120)
    def __init__(self):
        CompareTime = datetime.datetime.now()










