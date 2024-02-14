from ishiro.account.saver.serializers import SaverSerializer
from ishiro.user.models import User
from ishiro.user.serializers import UserSerializer
from rest_framework import viewsets, permissions


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = SaverSerializer
    permissions_class = ()
    http_method_names = ["post"]
    queryset = User.objects.all()

    
