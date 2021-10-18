"""[summary]
"""

from django.db.models.fields import CharField, DecimalField, IntegerField
from .model_basemodel import BaseModel
from django.db import models
from djmoney.models.fields import MoneyField
# from .model_body import Body
# from .model_styles import Styles


class Quotation(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    size = models.IntegerField()
    body_part = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    total_time = models.IntegerField(default=0)
    total_price = MoneyField(
                                    max_digits=8,
                                    decimal_places=0,
                                    default_currency='COP',
                                    default=0
                                    )

    class Meta:
        app_label = 'api_quotation'

    # def time_calculator(self):
