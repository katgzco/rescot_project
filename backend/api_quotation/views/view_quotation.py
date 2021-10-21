from api_quotation.serializations.serializer_quotation import QuotationSerializer
from api_quotation.models.model_quotation import Quotation
from api_quotation.models.model_user import User
from api_quotation.serializations.serializer_user import UserSerializer
from api_quotation.models.model_artist import Artist
from api_quotation.serializations.serializer_artist import ArtistsSerializer

from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def quotation_list(request):
    if request.method == 'GET':
        quotation = Quotation.objects.all()

    quotation_serializer = QuotationSerializer(quotation, many=True)
    return JsonResponse(quotation_serializer.data, safe=False)

@api_view(['GET'])
def quotation_by_id(request, pk):

    if request.method == 'GET':
        try:
            quotation = Quotation.objects.filter(id=pk)
        except Quotation.DoesNotExist:
            return JsonResponse(
                                {'message': 'The quotation does not exist'},
                                status=status.HTTP_404_NOT_FOUND
                                )
        quotation_serializer = QuotationSerializer(quotation, many=True)
        return JsonResponse(quotation_serializer.data, safe=False)


@api_view(['POST'])
def quote_creation(request):

    if request.method == 'POST':
        try:
            artist_id = request.data['artist_id']['id']
        except Artist.DoesNotExist:
            return JsonResponse(
                                {'message': 'The artist does not exist'},
                                status=status.HTTP_404_NOT_FOUND
                                )
        artist_query = Artist.objects.get(pk=artist_id)
#        print(request.data['quotation'])
        quotation_serializer = QuotationSerializer(data=request.data['quotation'])
        user_serializer = UserSerializer(data=request.data['user'])
#        print(quotation_serializer)
        if quotation_serializer.is_valid() and user_serializer.is_valid():
            user_instance = user_serializer.save()
            quotation_instance = quotation_serializer.save(fk_user=user_instance, fk_artist=artist_query)
            time_cm2 = quotation_instance.time_estimator()
            price_cm2 = quotation_instance.price_estimator(artist_id)

            dict_ = {"price" : price_cm2, "time" : time_cm2}
            return JsonResponse(
                                dict_,
                                status=status.HTTP_201_CREATED,
                                safe=False
                                )
        return JsonResponse(
                            quotation_serializer.errors,
#                            user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )
