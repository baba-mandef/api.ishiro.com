from django.db import models
from ishiro.user.models import User
from ishiro.account.models import AccountMixin


class Saver(AccountMixin, User):
    user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    currency = models.CharField(max_length=3)

  

    class Meta:
        managed = True
