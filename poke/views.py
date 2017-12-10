from django.views import generic
from .models import  Pokemon,Compare
from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.views.generic.edit import CreateView

def IndexView(request):
    extra_context = {"LastCompares" : Compare.objects.all().order_by("-CompareTime")[0:3] , "object_list":Pokemon.objects.order_by('?').all()[0:6]}
    template_name = 'poke/index.html'
    return render(request, template_name, extra_context)


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

def PokeDetail(request, pk):
     # model = Pokemon.objects.get(pk)
     model = get_object_or_404(Pokemon, pk=pk)
     template_name = 'poke/detail.html'
     return render(request, template_name, {"object": model,"Similars": Pokemon.objects.filter(skill_type=model.skill_type).exclude(
                                                   pk=pk).order_by("?")[0:3]})

def CompareDetail(request, pk):
    # model = Pokemon.objects.get(pk)
    model = get_object_or_404(Compare, pk=pk)
    template_name = 'poke/comparedetail.html'
    return render(request, template_name,
                  {"object": model, "Similars": Compare.objects.filter(First=model.First).order_by("?")[0:3]})

def CompareFast(request,first,second):
    new = Compare()
    new.First = get_object_or_404(Pokemon,pk=first)
    new.Second=get_object_or_404(Pokemon,pk=second)
    new.SpecialName = ""
    new.save()
    return redirect("poke:compareDetail", pk=new.pk)


class CompareCreate(CreateView):
    model = Compare
    template_name = "poke/compare_form.html"
    fields = ["First","Second","SpecialName"]