from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from ishiro.extra.utils import uuid_generator


class IshiroObjectManager(models.Manager):
    
    def get_by_public_id(self, public_id, **kwargs):
        error = "{self.model.__name__} does not exist"

        if public_id=="undefined":
            raise ObjectDoesNotExist(error)
        qs = self.filter(**kwargs)
        
        try:
            instance = qs.get(public_id=public_id)
        except(ObjectDoesNotExist, ValidationError, ValueError):
            raise ObjectDoesNotExist(error)
        return instance


class IshiroObject(models.Model):

    public_id = models.UUIDField(default=uuid_generator, unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = IshiroObjectManager()

    class Meta:
        abstract = True
