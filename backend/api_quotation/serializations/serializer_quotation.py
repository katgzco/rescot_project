from rest_framework import serializers
from api_quotation.models.model_quotation import Quotation

class QuotationSerializer(serializers.ModelSerializer):
	artist=serializers.StringRelatedField(many=True)

	class Meta:
		model = Quotation
		fields = ['id', 'size', 'body_part', 'style', 'artist']
