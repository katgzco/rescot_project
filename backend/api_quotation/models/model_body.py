"""[summary]
"""

from django.db.models.fields import CharField
from .model_basemodel import BaseModel
from .model_artist import Artist
from django.db import models


class Body(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50)
    difficulty = models.IntegerField()
    fk_artist = models.ManyToManyField(Artist)

    class Meta:
        app_label = 'api_quotation'
