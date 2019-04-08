from datetime import timedelta, date
import re


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


def convert_distance(distance):
    """Covert distance string or int to float"""
    if not distance:
        return None
    if isinstance(distance, str):
        find_digit = re.match(r"\d*", distance.strip())
        result = find_digit.group()
        if result.isnumeric():
            return float(result)
        elif distance.strip().lower() == "maraton":
            return 42.1
        elif distance.strip().lower() in ["połmaraton", "polmaraton",
                                          "półmaraton"]:
            return 21.05
        else:
            return None

    return float(distance)
