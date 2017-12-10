from django.conf.urls import url
from . import views

app_name = 'poke'
urlpatterns = [
    # /music/
    url(r'^$' ,views.IndexView.as_view(),name='index'),
    url(r'^pokemonlist/$', views.PokemonList.as_view(), name='pokemonList'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PokeDetail, name='pokeDetail'),
    url(r'^compDetail/(?P<pk>[0-9]+)/$', views.CompareDetail, name='compareDetail'),
    url(r'^story/$', views.StoryView.as_view(), name='story'),
    url(r'^generations/$', views.GenerationsView.as_view(), name='generations'),
    url(r'^compare/$', views.CompareCreate.as_view(), name='compare'),
    # /music/<album_id>/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add
    #url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add')

]
