"""[summary]
"""

from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import ImageField
from . import BaseModel


class Quotation(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    size = models.IntegerField()
    body = models.CharField(max_length=50, blank=False)
    style = models.CharField(max_length=50, blank=False)
    total_time = models.DecimalFields()
    total_price = models.DecimalField()

    class Meta:
        app_label = 'api_quotation'

    def __str__(self):
        return f'{self.name} _ {self.mail} _ {self.phone} _ {self.address}'
