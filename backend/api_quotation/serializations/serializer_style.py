from rest_framework import serializers
from api_quotation.models.model_styles import Styles


class StyleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Styles
		fields = ['id', 'name', 'time_cm2', 'price_cm2']
