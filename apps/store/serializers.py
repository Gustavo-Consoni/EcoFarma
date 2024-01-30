from rest_framework import serializers
from apps.store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'brand', 'category', 'price', 'total_rating', 'total_reviews', 'stock', 'description']

    def get_brand(self, obj):
        return obj.brand.name
    
    def get_category(self, obj):
        return obj.category.name
    
    def get_price(self, obj):
        return obj.price / 100
