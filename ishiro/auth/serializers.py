from rest_framework import serializers
from django.contrib.auth import authenticate
from importlib import import_module
from ishiro.account.saver.models import Saver

class LoginSerializer(serializers.Serializer):
    """
    Token authentication serializer class
    """

    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=150, write_only=True)

    def validate(self, attrs):
        """
        Authentication serializer validation
        """
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            # check if user provide correct credentials
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                error = "Unable to login user with thees credentials"
                raise serializers.ValidationError(error, code="authorization")

        else:
            error = "User must provide a username and a password"
            raise serializers.ValidationError(error, code="authorization")
        account_data = self.get_account_data(user)
        attrs["user"] = user
        attrs["account_data"] = account_data

        return attrs

    def get_account_data(self, user):
        
        account = Saver.objects.get(user=user)
        account_data = {}
       
        account_data["public_id"] = user.public_id
        account_data["id"] = user.id
        account_data["email"] = user.email
        account_data["name"] = user.name
        account_data["avatar"] = account.avatar.url
        account_data["balance"] = account.balance
        account_data["currency"] = account.currency

        return account_data
    


