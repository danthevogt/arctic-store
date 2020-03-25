from rest_framework import serializers
from api.models import Product, Category, Sale

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['name','address1', 'address2', 'city', 'state', 'zipcode', 'total', 'items', 'payment_intent']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id','category','filename','name','description','price']
