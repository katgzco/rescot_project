""" Module that contain the create_event view """


from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .api_service import api_service
from .info_quotation import info_quotation
from .time_converter import time_converter


@api_view(['POST'])
def create_event(request):
    """view to create event acocording to the request data

    Args:
        request (obj): object containing request information
    """

    event_data = info_quotation(request.data["quotation_id"])
    print(event_data)
    try:
        user_data = event_data['user_data']
        quotation_data = event_data['quotation_data']
        artist_data = event_data['artist_data']
        event_year = request.data['year']
        event_month = request.data['month']
        event_day = request.data['day']

        event_duration = request.data['total_time']
        start_time = request.data['time_event']
    except KeyError:
        return JsonResponse(
            {'message': 'Incorrect data'},
            status=status.HTTP_404_NOT_FOUND
        )

    end_time = time_converter(start_time, event_duration)

    start_date_event = event_year + '-' + event_month + \
        '-' + event_day + 'T' + start_time

    end_date_event = event_year + '-' + event_month + \
        '-' + event_day + 'T' + end_time
    print()
    print(str(artist_data[0].phone))
    print()
    event = {
        'summary': user_data[0].name + ' Tattoo appointment',
        'location': artist_data[0].address,
        'description': 'Event created atomatically by the Rescot system',
        'colorId': 5,
        'status': 'confirmed',
        'transparency': 'opaque',
        'start': {
            'dateTime': start_date_event + ':00-05:00'
        },
        'end': {
            'dateTime': end_date_event + ':00-05:00'
        },
        'attachments': [
            {
                'fileUrl': 'https://drive.google.com/file/d/1sOuWO5QuJbEJ82td0SPXOJDt8VpMC6kp/view?usp=sharing',
                'title': 'rescot miniatura'
            }
        ],
        'attendees': [
            {
                'email': artist_data[0].mail,
                'responseStatus': 'accepted'
            },
            {
                'email': user_data[0].mail,
                'comment': 'If you need to change the appointment please contact the artist to reschedule: ' + str(artist_data[0].phone)
            }
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    service_data = api_service()
    service = service_data[0]
    calendar_id = service_data[1]

    maxAttendees = 5
    sendNotification = True
    sendUpdate = "none"
    supportsAttachments = True

    event = service.events().insert(
        calendarId=calendar_id,
        maxAttendees=maxAttendees,
        sendNotifications=sendNotification,
        sendUpdates=sendUpdate,
        supportsAttachments=supportsAttachments,
        body=event
    ).execute()
    print('Event created: %s' % (event.get('htmlLink')))

    return JsonResponse(
        {"message": "Event successfully created"},
        status=status.HTTP_201_CREATED,
        safe=False
    )
