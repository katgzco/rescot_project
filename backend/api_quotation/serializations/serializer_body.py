from rest_framework import serializers
from api_quotation.models.model_body import Body

class BodySerializer(serializers.ModelSerializer):
	class Meta:
		model = Body
		fields = ['id', 'name', 'difficulty']
