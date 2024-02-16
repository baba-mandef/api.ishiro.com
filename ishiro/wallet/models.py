from django.db import models
from ishiro.abstract.models import IshiroObject
from ishiro.account.saver.models import Saver


class Wallet(models.Model):
    label = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    # category = models.ForeignKey()
    owner = models.ForeignKey(Saver, on_delete=models.CASCADE)

