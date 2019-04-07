from datetime import timedelta, date


def string_to_timedelta(delta_string):
    """Change string format 00:00:00 to timedelta instance"""
    ti = delta_string.split(':')
    try:
        hour = int(ti[0])
        minute = int(ti[1])
        second = int(ti[2])
    except ValueError:
        time_delta = None
    except IndexError:
        time_delta = None
    else:
        time_delta = timedelta(hours=hour, minutes=minute, seconds=second)
    return time_delta


def string_to_date(date_string):
    """Change string format YYYY-MM-DD to date instance"""
    year, month, day = date_string.split('-')
    return date(int(year), int(month), int(day))
