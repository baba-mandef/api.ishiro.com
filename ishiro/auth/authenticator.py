from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from ishiro.extra.tools import generate_token, check_key, validate_jwt
from ishiro.auth.models import Token


class JWTAuth(BaseAuthentication):
    """
    Custom JWT authentication for authenticate an user
    """

    keyword = "Bearer"
    token_model = Token
    message = "Invalid username or password"

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            # check out the authorization header integrity
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed(self.message)

        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed(self.message)

        try:
            token = auth[1].decode()

        except UnicodeError:
            raise exceptions.AuthenticationFailed(self.message)

        return self.authenticate_credentials(token)

    def authenticate_header(self, request):
        # Return the string that will be use as the value of WWW-Authenticate
        return self.keyword

    def authenticate_credentials(self, token):
        payload = validate_jwt(token)

        user_model = get_user_model()

        try:
            user = user_model.objects.get_by_public_id(public_id=payload["id"])
        except (user_model.DoesNotExist, KeyError):
            raise exceptions.AuthenticationFailed(self.message)

        try:
            key = user.auth_token.key
        except self.token_model.DoesNotExist:
            raise exceptions.AuthenticationFailed(self.message)

        if not check_key(key, payload["key"]):
            raise exceptions.AuthenticationFailed(self.message)

        if not user.is_active:
            raise exceptions.AuthenticationFailed("Inactive account")
        return user, key

    @classmethod
    def get_token(cls, user, token_id=None, force_refresh=True):
        try:
            auth_token = cls.token_model.objects.get(user=user)

        except ObjectDoesNotExist:
            auth_token = cls.token_model.objects.create(user=user)
        else:
            auth_token.regenerate(force_refresh=force_refresh)

        public_id = user.public_id
        return cls.generate_jwt(auth_token, public_id.hex)

    @classmethod
    def generate_jwt(cls, token, public_id):
        return generate_token(token.key, token.refresh, token.public_id.hex, public_id)