from rest_framework import serializers
from api_quotation.models.model_user import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'name', 'phone', 'mail']
