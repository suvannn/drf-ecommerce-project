from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing Catergory

    """

    querset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serilizer = CategorySerializer(self.querset, many=True)
        return Response(serilizer.data)
