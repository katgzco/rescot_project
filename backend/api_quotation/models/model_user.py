"""[summary]
"""

from django.db import models
from django.db.models.fields import CharField, EmailField
from . import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from .model_quotation import Quotation


class User(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """

    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(max_length=254, blank=False)
    phone = PhoneNumberField(blank=False)
    fk_quotation = models.OneToOneField(
        Quotation, related_name='user', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        app_label = 'api_quotation'

    def __str__(self):
        return f'{self.name} _ {self.mail} _ {self.phone}'
