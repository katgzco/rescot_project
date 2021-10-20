from django.urls import path
from api_quotation.views.view_artist import artist_list, artist_by_id, quotes_by_artist
from api_quotation.views.view_quotation  import quotation_list, quotation_by_id, quote_creation

urlpatterns = [
    path('artists', artist_list),
    path('artists/<uuid:pk>', artist_by_id),
    path('artists/quotation/<uuid:pk>',  quotes_by_artist),
    path('quotation', quotation_list),
    path('quotation/<uuid:pk>', quotation_by_id),
    path('quotation/create', quote_creation)
]
