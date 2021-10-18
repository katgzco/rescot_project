"""[summary]
"""

from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.fields import CharField, EmailField
from .model_basemodel import BaseModel
from .model_quotation import Quotation
from django.db import models


class User(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    fk_quotation = models.OneToOneField(
        Quotation, related_name='user', on_delete=models.CASCADE, default='')

    class Meta:
        app_label = 'api_quotation'
