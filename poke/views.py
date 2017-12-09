from django.views import generic
from .models import  Pokemon
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader



def PokeDetail(request,pk):
    #model = Pokemon.objects.get(pk)
    model = get_object_or_404(Pokemon, pk=pk)
    template_name = 'poke/detail.html'
    return render(request, template_name, {"object":model,"Similars": Pokemon.objects.filter(skill_type=model.skill_type).order_by("?")[0:3]})

class IndexView(generic.ListView):
    template_name = 'poke/index.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by('?').all()[0:6]

class PokemonList(generic.ListView):
    template_name = 'poke/pokemonlist.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by().all()


class StoryView(generic.TemplateView):
    template_name = 'poke/story.html'


class GenerationsView(generic.ListView):
    template_name = 'poke/generations.html'
    def get_queryset(self):
        return  Pokemon.Generation.values