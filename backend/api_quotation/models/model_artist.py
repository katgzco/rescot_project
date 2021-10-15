"""[summary]
"""

from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.fields import CharField, EmailField
from .model_quotation import Quotation
from .model_basemodel import BaseModel
from django.db import models


class Artist(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False, default='')
    mail = models.EmailField(max_length=254, blank=False)
    phone = PhoneNumberField(blank=False)
    address = models.CharField(max_length=50, blank=False)
    fk_quotation = models.ForeignKey(
        Quotation, related_name='artist', on_delete=models.CASCADE, default='')

    class Meta:
        app_label = 'api_quotation'

    def __str__(self):
        return f'{self.name} _ {self.lastname} _ {self.mail} _ {self.phone} _ {self.address}'
