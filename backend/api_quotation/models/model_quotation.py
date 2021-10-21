"""[summary]
"""

from django.db.models.fields import CharField, DecimalField, IntegerField
from .model_basemodel import BaseModel
from .model_artist import Artist
from .model_body import Body
from .model_styles import Styles
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

#    def __repr__(self):
#        return "id:{}, artist_name:{}, user_name:{}".format(self.id, self.fk_artist, self.fk_user)


    def time_estimator(self):
        cm2 = self.size
        if cm2 <= 7:
            estimated_time = str(1,)
        elif cm2 <= 15:
            estimated_time = str(3, 4)
        else:
            estimated_time = str(5, 6)

        return estimated_time

    def price_estimator(self, artist_id):
        cm2 = self.size
        style = self.style.lower()
        body_part = self.body_part

        if cm2 <= 7:

            if style == 'black':
                price = 180,000

            if style == 'color':
                price = 220,000
        else:

            artist_style = Styles.objects.filter(fk_artist__id = artist_id, name = style)
            body_difficulty = Body.objects.filter(fk_artist__id = artist_id, name = body_part)
            price = artist_style.price_cm2 * cm2 * body_difficulty.difficulty

        return str(price)
