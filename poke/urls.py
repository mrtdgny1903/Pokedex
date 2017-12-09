from django.conf.urls import url
from . import views

app_name = 'poke'
urlpatterns = [
    # /music/
    url(r'^$' ,views.IndexView.as_view() ,name='index'),
    url(r'^PokemonList/$', views.PokemonList.as_view(), name='PokemonList'),
    url(r'^Detail/(?P<pk>[0-9]+)/$', views.PokeDetail.as_view(), name='PokeDetail'),
    url(r'^Story/$', views.StoryView.as_view(), name='Story'),
    url(r'^Generations/$', views.StoryView.as_view(), name='Generations'),
    # /music/<album_id>/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add
    #url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add')

]
