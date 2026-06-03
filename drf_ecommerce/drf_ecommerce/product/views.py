from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing Catergory

    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # @extend_schema(responses=CategorySerializer)
    # def list(self, request):
    #     serializer = CategorySerializer(self.queryset, many=True)
    #     return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
