from django.db import models
from ishiro.user.models import User
from ishiro.account.models import AccountMixin


class Saver(AccountMixin, User):
    user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10)

  

    class Meta:
        managed = True
