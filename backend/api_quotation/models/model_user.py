"""[summary]
"""

from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.fields import CharField, EmailField
from .model_basemodel import BaseModel
from django.db import models


class User(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=250)
    mail = models.EmailField(max_length=254)
    phone = PhoneNumberField()

    class Meta:
        app_label = 'api_quotation'
