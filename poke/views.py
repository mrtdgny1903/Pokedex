from django.views import generic
from .models import  Pokemon


class IndexView(generic.ListView):
    template_name = 'poke/index.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by('?').all()[0:6]

class PokemonList(generic.ListView):
    template_name = 'poke/pokemonlist.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by().all()

class PokeDetail(generic.DetailView):
    model = Pokemon
    template_name = 'poke/detail.html'


class StoryView(generic.TemplateView):
    template_name = 'poke/story.html'


class GenerationsView(generic.ListView):
    template_name = 'poke/generations.html.html'
