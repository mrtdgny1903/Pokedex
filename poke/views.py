from django.views import generic
from .models import  pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'poke/index.html'
    def get_queryset(self):
        return  pokemon.objects.all()
