from rest_framework import serializers
from ishiro.activity.models import Activity
from ishiro.budget.models import Budget


class ActivitySerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        context = self.context
        _activity_type = context.get('activity_type')
        category_type = attrs.get('category').category_type

        if _activity_type != category_type:
            raise serializers.ValidationError(
                {'activity_type': 'Activity type must be the same as category type'})
        else:
            attrs['activity_type'] = _activity_type

        return attrs

    def create(self, validated_data):
        activity = Activity.objects.create(**validated_data)
        _activity_type = self.context.get('activity_type')
        wallet = activity.wallet
        amount = activity.amount
        owner = wallet.owner
        
        
        

        if _activity_type == 'income':
            wallet.balance += amount
            owner.balance += amount
        elif _activity_type == 'expense':
            wallet.balance -= amount
            owner.balance -= amount

            category = activity.category
            activity_month = activity.created_at.month
            budget = Budget.objects.filter(category=category, period__month=activity_month).first()

            budget.spent += amount
            budget.remaining -= amount
            budget.save()

        wallet.save()
        owner.save()

        return activity

    class Meta:
        model = Activity
        fields = ['id', 'public_id', 'label',
                  'amount', 'description', 'category', 'wallet', 'activity_type',]

        extra_kwargs = {
            'public_id': {'read_only': True, 'required': False, },
            'id': {'read_only': True, 'required': False, },
            'activity_type': {'read_only': True, 'required': False, },
        }
