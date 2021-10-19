from rest_framework import serializers
from api_quotation.models.model_artist import Artist

class ArtistsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = '__all__'
