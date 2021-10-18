"""[summary]
    """

from django.db import models
import uuid


class BaseModel(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'api_quotation'

    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
