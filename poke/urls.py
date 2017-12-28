from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'poke'
urlpatterns = [
        # /music/
    url(r'^$' ,views.IndexView,name='index'),
    url(r'^all/$', views.PokemonList.as_view(), name='pokemonList'),
    url(r'^all/(?P<generation>[\w\-]+)/$', views.GenerationPokeList, name='pokemonListGenerations'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PokeDetail, name='pokeDetail'),
    url(r'^compDetail/(?P<pk>[0-9]+)/$', views.CompareDetail, name='compareDetail'),
    url(r'^story/$', views.StoryView.as_view(), name='story'),
    url(r'^generations/$', views.GenerationsView.as_view(), name='generations'),
    url(r'^compare/$', views.CompareCreate.as_view(), name='compare'),
    url(r'^compare/(?P<first>[0-9]+)/(?P<second>[0-9]+)/$', views.CompareFast, name='compareFast'),
    url(r'^beTrainer/$', views.UserFormView.as_view(), name='be_trainer'),
    url(r'^login/$', auth_views.login, {'template_name': 'poke/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,  {'next_page': "poke:index"},  name='logout'),
    url(r'^trainer/$', views.TrainerDetail, name='trainerDetail'),

    url(r'^addToTrainer/(?P<pk>[0-9]+)/$', views.addToTrainer, name='addToTrainer'),
    url(r'^RemovePokemon/(?P<pk>[0-9]+)/$', views.RemovePokemon, name='RemovePokemon'),


]
