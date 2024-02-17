from django.db import models
from ishiro.abstract.models import IshiroObject
from ishiro.account.saver.models import Saver
from ishiro.category.models import Category


class Wallet(IshiroObject):
    label = models.CharField(max_length=150)
    balance = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name="wallet_category", on_delete=models.CASCADE)
    owner = models.ForeignKey(Saver, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.label} - {self.balance}"


