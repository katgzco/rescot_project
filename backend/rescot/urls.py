"""rescot URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from api_quotation.views import artist_list, artist_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/artists', artist_list),
    path('api/v1/artists/<str:name>', artist_by_id),
]
