from rest_framework import serializers
from ishiro.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'public_id', 'label',
                  'description', 'icon', 'category_type',]
        extra_kwargs = {
            'public_id': {'read_only': True, 'required': False, },
            'id': {'read_only': True, 'required': False, },
        }
