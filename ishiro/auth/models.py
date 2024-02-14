import binascii
import os

from django.db import models
from django.conf import settings

from ishiro.extra.tools import uuid_generator


class Token(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid_generator)
    key = models.CharField(max_length=40)
    refresh = models.CharField(max_length=40, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="auth_token",
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
            self.refresh = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def regenerate(self, force_refresh=False):
        self.key = self.generate_key()
        if force_refresh:
            self.refresh = self.generate_key()
        self.save()

    def __str__(self):
        return self.key

    class Meta:
        db_table = "auth.auth_token"
        managed = True
