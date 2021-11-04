from django.urls import path
from calendarApp.views.view_availability import list_availability
from calendarApp.views.view_eventCreation import create_event
from django.urls import re_path


urlpatterns = [
    re_path('availability/?$', list_availability),
    re_path('creation/?$', create_event)
]
