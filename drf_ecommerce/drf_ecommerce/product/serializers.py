from rest_framework import serializers
from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), write_only=True
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )

    brand_detail = BrandSerializer(source="brand", read_only=True)
    category_detail = CategorySerializer(source="category", read_only=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "is_digital",
            "brand",
            "category",
            "brand_detail",
            "category_detail",
        ]
