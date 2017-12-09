from django.views import generic
from .models import  Pokemon,Trainer
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'poke/index.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by('?').all()[0:6]

class PokemonList(generic.ListView):
    template_name = 'poke/pokemonlist.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by().all()

class TrainerList(generic.ListView):
    template_name = 'poke/trainerlist.html'
    def get_queryset(self):
        return  Trainer.objects.order_by().all()

class TrainerProfil(generic.DetailView):
    model = Trainer
    template_name = 'poke/profil.html'

class PokeDetail(generic.DetailView):
    model = Pokemon
    template_name = 'poke/detail.html'

class StoryView(generic.View):
    template_name = 'poke/story.html'

class GenerationsView(generic.ListView):
    template_name = 'poke/generations.html.html'
