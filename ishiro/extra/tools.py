from uuid import uuid4
import random
from hashlib import sha256
from datetime import datetime, timedelta
import jwt
from django.conf import settings


def hash_key(key):
    return sha256(key.encode()).hexdigest()

def check_key(key, hashed):
    return hashed == hash_key(key)

def uuid_generator():
    return uuid4()


def generate_random_digits(n):
    return "".join(map(str, random.sample(range(0, 10), n)))


def generate_token(key, refresh, token_id, public_id, lifetime=None):
   
    if lifetime is None:
        lifetime = settings.JWT_TOKEN_VALIDITY_TIME

    token_auth = generate_token_jwt(
        key, 
        public_id,  
        token_id, 
        lifetime)

    token_refresh = generate_token_jwt(
        refresh,
        public_id, 
        token_id, 
        settings.JWT_REFRESH_TOKEN_VALIDITY_TIME
        )
    return token_auth, token_refresh



def generate_token_jwt(key, id_, token_id, lifetime):
    payload = {
        "key": hash_key(key),
        "exp": datetime.utcnow() + timedelta(minutes=lifetime),
        "id": id_,
        "token": token_id,
        "iat": datetime.utcnow(),
        "iss": "ishiro.bj"
    }
    return jwt.encode(payload, hash_key(settings.JWT_SECRET), algorithm="HS256")


def validate_jwt(token_jwt):
    try:
        payload = jwt.decode(
            token_jwt, hash_key(settings.JWT_SECRET),
            issuer="ishiro.bj",
            options={"required": ["exp", "iat", "iss"]},
            algorithms=["HS256"],
        )
    except (
        jwt.ExpiredSignatureError,
        jwt.DecodeError,
        jwt.InvalidIssuerError,
        jwt.MissingRequiredClaimError,
        jwt.InvalidIssuedAtError
    ):
        return {}
    else:
        return payload
