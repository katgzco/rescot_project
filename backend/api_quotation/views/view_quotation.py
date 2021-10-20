from api_quotation.serializations.serializer_quotation import QuotationSerializer
from api_quotation.models.model_quotation import Quotation
from api_quotation.models.model_user import User
from api_quotation.serializations.serializer_user import UserSerializer

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
            print(quotation)
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
        quotation_serializer = QuotationSerializer(data=request.data[0])
        if quotation_serializer.is_valid():
            obj = quotation_serializer.save()
            quotation_user = UserSerializer(data=request.data[1])
            if quotation_user.is_valid():
                quotation_user.save(fk_quotation=obj)
                dict_ = {"price_bycm2" : 34, "time_bycm2" : 1 }
                tmp_response = [dict_, quotation_serializer.data, quotation_user.data]
                return JsonResponse(
                                tmp_response,
                                status=status.HTTP_201_CREATED,
                                safe=False
                                )
        return JsonResponse(
                            quotation_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
