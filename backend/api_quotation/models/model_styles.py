"""[summary]
"""

from django.db.models.fields import CharField, DecimalField
from .model_basemodel import BaseModel
from .model_artist import Artist
from django.db import models


class Styles(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50)
#    time_cm2 = models.IntegerField()
    price_cm2 = models.IntegerField() # money field
    fk_artist = models.ManyToManyField(Artist)

    class Meta:
        app_label = 'api_quotation'
