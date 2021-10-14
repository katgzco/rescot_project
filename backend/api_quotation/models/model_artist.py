"""[summary]
"""

from django.db import models
from django.db.models.fields import CharField, EmailField
from . import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class Artist(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(max_length=254, blank=False)
    phone = PhoneNumberField(blank=False)
    address = models.CharField(max_length=50, blank=False)

    class Meta:
        app_label = 'api_quotation'

    def __str__(self):
        return f'{self.name} _ {self.mail} _ {self.phone} _ {self.address}'
