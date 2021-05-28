from django.contrib import admin

# Register your models here.
from .models import Client
from .models import Offre
admin.site.register(Client)
admin.site.register(Offre)