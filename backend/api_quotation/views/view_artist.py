from api_quotation.serializations.serializer_artist import ArtistsSerializer
from api_quotation.serializations.serializer_quotation import QuotationSerializer
from api_quotation.serializations.serializer_user import UserSerializer
from api_quotation.serializations.serializer_style import StyleSerializer
from api_quotation.serializations.serializer_body import BodySerializer
from api_quotation.models.model_artist import Artist
from api_quotation.models.model_body import Body
from api_quotation.models.model_styles import Styles
from api_quotation.models.model_quotation import Quotation
from api_quotation.models.model_user import User
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()

    artists_serializer = ArtistsSerializer(artists, many=True)
    return JsonResponse(artists_serializer.data, safe=False)

@api_view(['GET'])
def artist_by_id(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return JsonResponse(
                            {'message': 'The artist does not exist'},
                            status=status.HTTP_404_NOT_FOUND
                            )
    if request.method == 'GET':
        artist_serializer = ArtistsSerializer(artist)
        full_dict = artist_serializer.data

        styles = Styles.objects.filter(fk_artist=pk).values_list('name', flat=True)
        styles_list = [style for style in styles]
        full_dict['styles'] = styles_list

        body_parts = Body.objects.filter(fk_artist=pk).values_list('name', flat=True)
        body_list = [body_part for body_part in body_parts]
        full_dict['body_part'] = body_list

        return JsonResponse(full_dict)

@api_view(['GET'])
def quotes_by_artist(request, pk):
    try:
        quotation = Quotation.objects.filter(fk_artist==pk)
    except Quotation.DoesNotExist:
        return JsonResponse(
                            {'message': 'The quotation does not exist'},
                            status=status.HTTP_404_NOT_FOUND
                            )
    if request.method == 'GET':
        quotation_serializer = QuotationSerializer(quotation, many=True)
        return JsonResponse(quotation_serializer.data, safe=False)
