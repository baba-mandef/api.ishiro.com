from rest_framework.viewsets import ModelViewSet
from ishiro.wallet.serializers import WalletSerializer
from ishiro.account.saver.models import Saver
from rest_framework.response import Response
from rest_framework import status



class WalletViewSet(ModelViewSet):
    serializer_class = WalletSerializer
    http_method_names = ['get', 'post',]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        balance = validated_data['balance']
        saver = Saver.objects.filter(user__email=request.user.email).first()
        saver.balance = saver.balance + balance
        saver.save()
        self.serializer_class.Meta.model.objects.create(**validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get_queryset(self):

        model = self.serializer_class.Meta.model
        queryset = model.objects.filter(owner__email=self.request.user.email)    
        return queryset
