"""[summary]
"""

from django.db.models.fields import CharField, DecimalField, IntegerField
from .model_basemodel import BaseModel
from .model_artist import Artist
from .model_user import User
from django.db import models
from djmoney.models.fields import MoneyField


class Quotation(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    size = models.IntegerField()
    body_part = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    fk_artist = models.ForeignKey(
        Artist, related_name='artist_quotation', on_delete=models.CASCADE, blank=True, null=True)
    total_time = models.IntegerField(default=0)
    fk_user = models.OneToOneField(
        User, related_name='user_quotation', on_delete=models.CASCADE, blank=True, null=True)
    total_price = MoneyField(
        max_digits=8,
        decimal_places=0,
        default_currency='COP',
        default=0
    )
    description = models.CharField(max_length=255)

    class Meta:
        app_label = 'api_quotation'
