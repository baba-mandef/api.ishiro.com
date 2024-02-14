from ishiro.account.saver.models import Saver
from ishiro.account.serializers import AccountSerializer


class SaverSerializer(AccountSerializer):

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance

    class Meta:
        model = Saver
        fields = AccountSerializer.Meta.fields + (
            "currency",
        )
        extra_kwargs = AccountSerializer.Meta.extra_kwargs
        

