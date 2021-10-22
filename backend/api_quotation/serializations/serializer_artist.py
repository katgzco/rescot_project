from rest_framework import serializers
from api_quotation.models.model_artist import Artist
from api_quotation.models.model_body import Body
from api_quotation.serializations.serializer_body import BodySerializer


class ArtistsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Artist
		fields = ['id', 'name', 'mail', 'phone', 'address']
