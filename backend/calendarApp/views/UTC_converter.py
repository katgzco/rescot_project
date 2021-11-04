""" Module containgin the start_end_UTC_converter function """


import datetime
from datetime import datetime
import time

def start_end_UTC_converter(event):
    """Function to get the UTC start and end time from event
    and convert it into localtime datetime object

    Args:
            event (googleObj): calendar object

    Returns:
            [list]: start and end hours converted
    """
    start_utc = event['start'].get(
        'dateTime',
        event['start'].get(
            'date')
    )
    # converting str UTC time into datetime object
    start_utc = datetime.strptime(start_utc, '%Y-%m-%dT%H:%M:%SZ')

    end_utc = event['end'].get(
        'dateTime',
        event['end'].get('date')
    )  # getting UTC event end time

    # converting str UTC time into datetime object
    end_utc = datetime.strptime(end_utc, '%Y-%m-%dT%H:%M:%SZ')

    # Converting UTC datime object into localtime
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(
        now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    start = start_utc + offset
    end = end_utc + offset
    start_end_list = [start, end]

    return start_end_list
