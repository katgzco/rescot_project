"""rescot URL Configuration

"""
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_quotation.urls')),
    path('api/v1/calendar/', include('calendarApp.urls')),
]
