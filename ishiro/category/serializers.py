from rest_framework import serializers
from ishiro.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['label', 'description', 'icon', 'category_type',]
