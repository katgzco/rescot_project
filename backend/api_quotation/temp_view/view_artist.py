# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from api_quotation.serializations.serializer_artist import ArtistsSerializer
# from api_quotation.models.model_artist import Artist
# from django.http.response import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework import generics

# @api_view(['GET'])
# def artist_list(request):
# 	if request.method == 'GET':
# 		artists = Artist.objects.all()

# 	artists_serializer = ArtistsSerializer(artists, many=True)
# 	return JsonResponse(artists_serializer.data, safe=False)

# # class artist_test(generics.ListCreateAPIView):
# # 	queryset = artist.objects.all()
# # 	serializer_class = ArtistsSerializer
