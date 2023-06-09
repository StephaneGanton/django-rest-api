from rest_framework import serializers

from .models import Order, OrderItem

from produit.serializers import ProduitSerializer


class MyOrderItemSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer()

    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity',
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'items',
            'stripe_token',
            'paid_amount'
        )

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity',
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'items',
            'stripe_token',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order= order, **item_data)

        return order



            
            
            
            
            
            
            
            