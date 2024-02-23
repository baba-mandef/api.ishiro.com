from rest_framework import serializers
from ishiro.wallet.models import Wallet
from ishiro.category.models import Category
from ishiro.category.serializers import CategorySerializer


class WalletSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        category = attrs.get('category')
       
        type = category.category_type
        if type != 'wallet':
            raise serializers.ValidationError(
                    {'category': 'Category type must be a wallet'})
        return attrs

    class Meta:
        model = Wallet
        fields = ['public_id', 'label', 'balance', 'category', 'owner']
        extra_kwargs = {
            'public_id': {'read_only': True, 'required': False, },
        }
