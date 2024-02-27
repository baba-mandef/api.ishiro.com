from rest_framework import serializers
from ishiro.budget.models import Budget
from datetime import datetime


class BudgetSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs['spent'] = 0
        attrs['remaining'] = attrs['limit']
        category = attrs['category']
        period = attrs['period']
        if category.category_type!= 'expense':
            raise serializers.ValidationError({'category': 'Category type must be an expense'})

        if period.month < datetime.now().month:
            raise serializers.ValidationError({'period': 'Period must be greater or equal to the current month'})

        return attrs
    class Meta:
        model = Budget
        fields = ['id', 'public_id', 'limit', 
                  'category', 'spent', 'remaining', 'period', 'owner',]
        
        extra_kwargs = {
            'public_id': {'read_only': True,'required': False, },
            'id': {'read_only': True,'required': False, },
            'spent': {'read_only': True,'required': False, },
            'remaining': {'read_only': True,'required': False, },
        }
