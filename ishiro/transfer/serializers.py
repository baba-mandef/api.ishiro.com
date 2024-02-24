from rest_framework import serializers
from ishiro.transfer.models import Transfer


class TransferSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        source = attrs['wallet_source']
        receiver = attrs['receiver_wallet']
        if source == receiver:
            raise serializers.ValidationError({'wallet_source': 'Source and receiver wallets must be different'})
        if source.owner != receiver.owner:
            raise serializers.ValidationError({'wallet_source': 'Source and receiver wallets must be owned by the same user'})
        
        return attrs
    
    def create(self, validated_data):
        transfer = Transfer.objects.create(**validated_data)
        amount = validated_data['amount']
        transfer.wallet_source.balance-=amount
        transfer.receiver_wallet.balance+=amount
        transfer.save()
        transfer.wallet_source.save()
        transfer.receiver_wallet.save()
        return transfer
    

    class Meta:
        model = Transfer
        fields = ['id', 'public_id', 'label', 'amount',
                  'description', 'wallet_source', 'receiver_wallet']
        extra_kwargs = {
            'public_id': {'read_only': True, 'required': False, },
            'id': {'read_only': True, 'required': False, },
        }
