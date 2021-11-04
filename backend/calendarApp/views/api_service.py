""" Module to contain entry proint for calendar API """

from .Google import Create_Service


def api_service():
	"""function to retrieve calendar object information

	Returns:
		[list]: calendar object information
	"""
	CLIENT = "calendarApp/views/credentials.json"
	API_NAME = "calendar"
	API_VERSION = "v3"
	SCOPES = ["https://www.googleapis.com/auth/calendar"]

	service = Create_Service(CLIENT, API_NAME, API_VERSION, SCOPES)

	calendar_id = "kqbaf1dmbf3u7ofj6ll1tirci8@group.calendar.google.com" # method to find id

	return_data = [service, calendar_id]

	return return_data
