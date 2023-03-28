from rest_framework import serializers

from .models import Category, Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = [
            'id', 
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
        ]

class CategorySerializer(serializers.ModelSerializer):

    produits = ProduitSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id', 
            'name',
            'get_absolute_url',
            'produits'
        )