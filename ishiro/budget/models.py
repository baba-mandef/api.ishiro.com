from django.db import models
from ishiro.abstract.models import IshiroObject
from ishiro.category.models import Category
from ishiro.account.saver.models import Saver


class Budget(IshiroObject):
    limit = models.IntegerField()
    category = models.ForeignKey(Category, related_name="budget_category", on_delete=models.CASCADE)
    spent = models.IntegerField()
    remaining = models.IntegerField()
    period = models.DateField()
    owner = models.ForeignKey(Saver, on_delete=models.CASCADE)
    