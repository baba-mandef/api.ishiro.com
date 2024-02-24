from rest_framework.viewsets import ModelViewSet
from ishiro.wallet.serializers import WalletSerializer


class WalletViewSet(ModelViewSet):
    serializer_class = WalletSerializer
    http_method_names = ['get', 'post',]

    def get_queryset(self):

        model = self.serializer_class.Meta.model
        queryset = model.objects.filter(owner__email=self.request.user.email)    
        return queryset
