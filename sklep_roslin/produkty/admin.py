from django.contrib import admin
from .models import Kategoria, Tag, Produkt, Dostawa

admin.site.register(Kategoria)
admin.site.register(Tag)
admin.site.register(Produkt)
admin.site.register(Dostawa)
