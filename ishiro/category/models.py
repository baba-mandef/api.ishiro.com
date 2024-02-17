from django.db import models
from ishiro.abstract.models import IshiroObject
from ishiro.extra.enum import CategoryTypeEnum


class Category(IshiroObject):
    label = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True, blank=True)
    icon = models.CharField(max_length=15)
    color = models.CharField(max_length=10)
    category_type = models.CharField(max_length=10, choices=CategoryTypeEnum.items())


    def __str__(self) -> str:
        return f"{self.category_type}-{self.label}"
