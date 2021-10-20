from api_quotation.serializations.serializer_artist import ArtistsSerializer
from api_quotation.serializations.serializer_quotation import QuotationSerializer
from api_quotation.serializations.serializer_user import UserSerializer
from api_quotation.models.model_artist import Artist
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
        return JsonResponse(artist_serializer.data)

@api_view(['GET'])
def quotes_by_artist(request, pk):
    try:
        quotation = Quotation.objects.filter(artist__id=pk)
        print(quotation)
    except Quotation.DoesNotExist:
        return JsonResponse(
                            {'message': 'The quotation does not exist'},
                            status=status.HTTP_404_NOT_FOUND
                            )
    if request.method == 'GET':
        quotation_serializer = QuotationSerializer(quotation, many=True)
        return JsonResponse(quotation_serializer.data, safe=False)
