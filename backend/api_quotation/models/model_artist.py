"""[summary]
"""

from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.fields import CharField, EmailField
from .model_basemodel import BaseModel
from django.db import models


class Artist(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    phone = PhoneNumberField(blank=False)
    address = models.CharField(max_length=50)

    class Meta:
        app_label = 'api_quotation'
