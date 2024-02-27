from rest_framework import (viewsets, status)
from ishiro.category.serializers import CategorySerializer
from rest_framework.response import Response


class CategoryViewSet(viewsets.ViewSet):

    serializer_class = CategorySerializer


    def list(self, request, *args, **kwargs):
        category_type = kwargs.get('category_type')
        category = self.serializer_class.Meta.model
        queryset = category.objects.filter(category_type=category_type)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
