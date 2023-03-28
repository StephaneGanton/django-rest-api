from os import name
from django.db.models import Q
from django.http import Http404
#from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Produit
from .serializers import ProduitSerializer, CategorySerializer

class LatestProduitsList(APIView):

    def get(self, request, format=None):
        produits =  Produit.objects.all()[0:4]
        serializer = ProduitSerializer(produits, many=True)

        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Produit.objects.filter(category__slug = category_slug).get(slug=product_slug)
        except Produit.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProduitSerializer(product)

        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        produits = Produit.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProduitSerializer(produits, many=True)

        return Response(serializer.data)
    else:
        return Response({'produits': []})