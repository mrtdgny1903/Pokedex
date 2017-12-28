from django.views import generic
from .models import  Pokemon,Compare, Trainer
from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import *
def IndexView(request):
    extra_context = {"LastCompares" : Compare.objects.all().order_by("-CompareTime")[0:3] , "object_list":Pokemon.objects.order_by('?').all()[0:6]}
    template_name = 'poke/index.html'
    return render(request, template_name, extra_context)

class PokemonList(generic.ListView):
    template_name = 'poke/pokemonlist.html'
    extra_context = {"page_title" : "All Pokemons"}
    def get_queryset(self):
        return  Pokemon.objects.order_by().all()

def GenerationPokeList(request,generation):
    template_name = 'poke/pokemonlist.html'
    gType = 0
    for gen in Pokemon.Generation.keys():
        if Pokemon.Generation.get(gen) == generation:
            gType = gen


    objects = Pokemon.objects.filter(generation_type= gType)

    return render(request, template_name,
                  {"object_list": objects , "page_title" : generation +" Generation Pokemons" })




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
    return render(request, template_name,
                  {"object": model, "Similars": Pokemon.objects.filter(skill_type=model.skill_type).exclude(
                      pk=pk).order_by("?")[0:3]})





def addToTrainer(request, pk):
    # model = Pokemon.objects.get(pk)
    user = request.user
    model = get_object_or_404(Trainer, UserT=user)
    pokemon = get_object_or_404(Pokemon,pk=pk)
    model.Pokemons.add(pokemon)
    model.save()

    return redirect('poke:trainerDetail')

def RemovePokemon(request, pk):
    # model = Pokemon.objects.get(pk)
    user = request.user
    model = get_object_or_404(Trainer, UserT=user)
    pokemon = get_object_or_404(Pokemon,pk=pk)
    model.Pokemons.remove(pokemon)
    model.save()

    return redirect('poke:trainerDetail')


def TrainerDetail(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        model = get_object_or_404(Trainer, UserT = user)
        if model:
            template_name = 'poke/trainerDetail.html'
            return render(request, template_name,
                  {"object": model ,"pokemons" : model.Pokemons.all()})
    return redirect('poke:index')



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



class UserFormView(View):
    form_class = UserForm
    template_name = "poke/be_trainer.html"
    def get(self, request):
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()
            trainer = Trainer()
            trainer.Name = username
            trainer.UserT=user
            trainer.save()
            user = authenticate(username = username,password= password)

            if  user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('poke:index')


        return render(request,self.template_name,{'form':form})


class Login(View):
    form_class = AuthenticationForm
    template_name = "poke/be_trainer.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            control = AuthenticationForm(data=request.POST)
            if (control.is_valid()):
                user = authenticate(username=username, password=password)
                if user.is_active:
                    login(request, user)
                    return redirect('poke:index')
        return render(request, self.template_name, {'form': form})