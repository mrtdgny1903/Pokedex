from django.db import models
import datetime
from django.contrib.auth.models import User

class Pokemon(models.Model):

    Name = models.CharField(max_length=40)
    Picture = models.FileField(upload_to='images/')
    Height = models.FloatField()
    Weight = models.FloatField()
    Abilities =models.CharField(max_length=40)
    HP = models.IntegerField(default=10)
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

    def GetType(self):
        return self.Type[int(self.skill_type)][1]

    Gender = (
        ('0', 'Male'),
        ('1', 'Female'),
        ('2', '%50 Male %50 Female'),

    )
    gender_type = models.CharField(max_length=1, choices=Gender)

    def GetGender(self):
        return self.Gender[int(self.gender_type)][1]

    """ Generation = (
        ('0', 'I'),
        ('1', 'II'),
        ('2', 'III'),
        ('3', 'IV'),
        ('4', 'V'),
        ('5', 'VI'),
        ('6', 'VII'),

    ) """
    def GetGeneration(self):
        return self.Generation.get(self.generation_type)
    Generation = {
        '0' :'I',
        '1' :'II',
        '2' :'III',
        '3' :'IV',
        '4' :'V',
        '5' :'VI',
        '6' :'VII',
    }
    generation_type = models.CharField(max_length=1,choices=Generation.items())

    def __str__(self):
        return self.Name

class Trainer(models.Model):

    Name = models.CharField(max_length=40)
    UserT = models.OneToOneField(User,on_delete=models.CASCADE)
    Pokemons = models.ManyToManyField(Pokemon)


    def __str__(self):
        return self.Name

class Compare(models.Model):
         First = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="First")
         Second = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="Second",default=0)
         CompareTime = models.DateTimeField(default=datetime.datetime.now())
         SpecialName = models.CharField(max_length=120)
         def __str__(self):
             return self.First.Name+" Vs. " + self.Second.Name
         def get_absolute_url(self):
             return "/poke/"










