from django.contrib import admin
# Register your models here.

from .models import Category, Produit

admin.site.register(Category)
admin.site.register(Produit)
