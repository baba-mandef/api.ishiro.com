from ishiro.user.serializers import UserSerializer
from django.utils.timezone import now
from ishiro.extra.tools import generate_random_digits


class AccountSerializer(UserSerializer):
    def create(self, validated_data):
        validated_data.setdefault("is_active", True)
        validated_data.setdefault("activated", now())
        validated_data.setdefault("verified", None)
        validated_data.setdefault("verification_code", generate_random_digits(6))
        return super().create(validated_data)

    class Meta():
        model = None
        fields = UserSerializer.Meta.fields + (
            'deactivated_reason',
            'deactivated',
            'activated',
            'verified',
            'verification_code',
            'avatar',
        )
        extra_kwargs = UserSerializer.Meta.extra_kwargs | {
            'deactivated_reason': {'read_only': True},
            
            'activated': {'read_only': True},
            'deactivated': {'read_only': True},
            'verified':{'read_only': True},
            'verification_code':{'read_only': True}
        }
     

