from django.db import models
from ishiro.abstract.models import IshiroObject
from ishiro.wallet.models import Wallet


class Transfer(IshiroObject):
    label = models.CharField(max_length=150)
    amount = models.IntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    wallet_source = models.ForeignKey(Wallet, related_name="wallet_source")
    receiver_wallet = models.ForeignKey(Wallet, related_name="receiver_wallet")
    
