from django.contrib import admin
from .models import *

admin .site.register(Pokemon)
admin .site.register(Trainer)
admin .site.register(Compare)

# Register your models here.
