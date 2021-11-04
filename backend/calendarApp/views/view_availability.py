""" Module that contain the list_availability view """


from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

import time
import json
from .Google import convert_to_RFC_datetime
from .UTC_converter import start_end_UTC_converter
from .api_service import api_service
# from .info_quotation import info_quotation


@api_view(['POST'])
def list_availability(request):
    # def list_events_calendar(selected_date, quotation_data, service, calendar_id):
    """view to list the events from the day selected

    Args:
            request (obj): data about the request
    """
    print(request.data)
    list_response = []
    try:
        selected_year = int(request.data['year'])
        selected_month = int(request.data['month'])
        selected_day = int(request.data['day'])
        time_event = int(request.data['total_time'])
    except KeyError:
        return JsonResponse(
            {'message': 'Incorrect data'},
            status=status.HTTP_404_NOT_FOUND
        )

    startHour = 12  # 7:00 Colombian timezone
    finalHour = 22  # 17:00 Colombian timezone

    timeMin = convert_to_RFC_datetime(
        selected_year,
        selected_month,
        selected_day,
        startHour,
        00
    )

    timeMax = convert_to_RFC_datetime(
        selected_year,
        selected_month,
        selected_day,
        finalHour,
        00
    )

    service_data = api_service()
    service = service_data[0]
    calendar_id = service_data[1]

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=timeMin,
        timeMax=timeMax,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    free_hour_counter = 0

    # calendar_data = info_quotation(id_quotation)

    if not events:
        for i in range(0, finalHour - startHour):
            if i + time_event <= (finalHour - startHour):
                list_response.append(str((startHour - 5) + i) + ':00')
        return JsonResponse(
            list_response,
            status=status.HTTP_201_CREATED,
            safe=False
        )

    for event in events:
        # getting UTC event start end time
        start_end = start_end_UTC_converter(event)
        start = start_end[0]
        end = start_end[1]

        if (start.hour > (startHour) and events.index(event) == 0):
            time_between = start.hour - (startHour)
            if time_between >= time_event:
                for i in range(0, time_between):
                    if i + time_event <= time_between:
                        free_hour_counter += 1
                        list_response.append(str((startHour - 5) + i) + ':00')

        if (events.index(event) < (len(events) - 1)):
            next_event = events[events.index(event) + 1]

            # getting UTC event start end time
            start_end_next_event = start_end_UTC_converter(next_event)
            start_next_event = start_end_next_event[0]
            end_next_event = start_end_next_event[1]

            time_between = start_next_event.hour - end.hour

            if (time_between > 0 and time_between >= time_event):
                for i in range(0, time_between):
                    if i + time_event <= time_between:
                        free_hour_counter += 1
                        list_response.append(str((end.hour - 5 + i)) + ':00')

        if (end.hour < (finalHour) and events.index(event) == (len(events) - 1)):
            time_between = 0
            time_between = (finalHour) - end.hour
            if time_between >= time_event:
                for i in range(0, time_between):
                    if i + time_event <= time_between:
                        free_hour_counter += 1
                        list_response.append(str((end.hour - 5 + i)) + ':00')

    if free_hour_counter == 0:
        return JsonResponse(
            {'message': 'No availability'},
            status=status.HTTP_204_NO_CONTENT,
            safe=False
        )

    return JsonResponse(
        list_response,
        status=status.HTTP_201_CREATED,
        safe=False
    )
