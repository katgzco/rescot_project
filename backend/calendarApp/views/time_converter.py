""" Module containing time_converter function """

def time_converter(str_local_time, event_duration):
    """Function to convert start event time into end event time

    Args:
        str_local_time (str): time string to be converted
    """
    event_duration = int(event_duration)
    local_firts_digit = int(str_local_time[:2])
    UTC_converted = local_firts_digit + event_duration

    if UTC_converted < 10:
        UTC_converted = '0' + str(UTC_converted)
    elif UTC_converted == 24:
        UTC_converted = "00"
    elif UTC_converted == 25:
        UTC_converted = "01"
    elif UTC_converted == 26:
        UTC_converted = "02"
    elif UTC_converted == 27:
        UTC_converted = "03"
    elif UTC_converted == 28:
        UTC_converted = "04"
    elif UTC_converted == 29:
        UTC_converted = "05"
    elif UTC_converted == 30:
        UTC_converted = "06"
    elif UTC_converted == 31:
        UTC_converted = "07"
    elif UTC_converted == 32:
        UTC_converted = "08"
    elif UTC_converted == 33:
        UTC_converted = "09"
    else:
        UTC_converted = str(UTC_converted)

    return (UTC_converted + str_local_time[2:])
