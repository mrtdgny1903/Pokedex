from django.views import generic
from .models import  Pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'poke/index.html'
    def get_queryset(self):
        return  Pokemon.objects.order_by('?').all()[0:6]
