from rest_framework import serializers
from api_quotation.models.model_quotation import Quotation

class QuotationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Quotation
		fields = ['id', 'size', 'body_part', 'style', 'fk_artist', 'fk_user']
