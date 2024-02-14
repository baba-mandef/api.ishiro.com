from rest_framework import viewsets
from django.utils import timezone
from ishiro.auth.serializers import LoginSerializer
from ishiro.auth.models import Token
from ishiro.auth.authenticator import JWTAuth
from rest_framework import status, response
from rest_framework.permissions import AllowAny
from ishiro.account.saver.models import Saver


class ObtainAuthToken(viewsets.ViewSet):
    serializer_class = LoginSerializer
    http_method_names = ["post"]
    queryset = Token.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        account = serializer.validated_data.get("account_data")
        user.last_login = timezone.now()
        token = JWTAuth().get_token(user)
        account['token'] = token[0]
        account['refresh'] = token[1]
        user.save()
        return response.Response(
            data= account,
            status=status.HTTP_200_OK,
        )
