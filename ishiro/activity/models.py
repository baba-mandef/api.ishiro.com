from django.db import models
from ishiro.abstract.models import IshiroObject
from ishiro.extra.enum import ActivityTypeEnum
from ishiro.category.models import Category
from ishiro.wallet.models import Wallet


class Activity(IshiroObject):
    label = models.CharField(max_length=150)
    amount = models.IntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, related_name="activity_category", on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, related_name="activity_wallet", on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=10, choices=ActivityTypeEnum.items())
