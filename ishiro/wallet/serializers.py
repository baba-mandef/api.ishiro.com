from rest_framework import serializers
from ishiro.wallet.models import Wallet



class WalletSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        category = attrs.get('category')

        type = category.category_type
        if type != 'wallet':
            raise serializers.ValidationError(
                {'category': 'Category type must be a wallet'})
        return attrs
    
    def create(self, validated_data):
        wallet = Wallet.objects.create(**validated_data)
        owner = wallet.owner
        owner.balance += wallet.balance
        wallet.save()
        owner.save()
        return wallet

    class Meta:
        model = Wallet
        fields = ['id', 'public_id',  'label', 'balance', 'category', 'owner']
        extra_kwargs = {
            'public_id': {'read_only': True, 'required': False, },
            'id': {'read_only': True, 'required': False, },
        }
