from django.contrib import admin

import poke
from .models import *

admin.site.register(Pokemon)
admin.site.register(Trainer)
admin.site.register(Compare)


class pokeAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date']
    list_display_links = ['title', 'publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'text']

    class Meta:
        model = Pokemon


