"""[summary]
"""

from django.db.models.fields import CharField, DecimalField, IntegerField
from .model_basemodel import BaseModel
from django.db import models


class Quotation(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    size = models.IntegerField()
    body_part = models.CharField(max_length=50, blank=False)
    style = models.CharField(max_length=50, blank=False)
    total_time = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        app_label = 'api_quotation'

    def __str__(self):
        return f'{self.size} _ {self.body_part} _ {self.style}\
        {self.total_time} _ {self.total_price}'
