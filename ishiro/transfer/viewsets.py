from rest_framework import viewsets
from ishiro.transfer.serializers import TransferSerializer


class TransferViewSet(viewsets.ModelViewSet):
    serializer_class = TransferSerializer
    http_method_names = ['get', 'post', ]

    def get_queryset(self):

        model = self.serializer_class.Meta.model
        queryset = model.objects.filter(wallet_source__owner__email=self.request.user.email)
        return queryset
