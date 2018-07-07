from datetime import datetime, timedelta


class MinuteCalculation:
    premium = 0
    nonPremium = 0


def is_premium(current):
    if current.isoweekday() == 6 or current.isoweekday() == 7:
        return True

    if current.hour < 7 or current.hour > 19:
        return True

    return False


def calculate_doctors_minutes(start, finish):
    if start.minute != 0 or finish.minute != 0:
        raise NotImplementedError("The spec requires start/finish times have a minute value of 0.")

    if start > finish:
        raise ValueError("The start time must be before the finish time! ")

    ret = MinuteCalculation()
    current = start

    while current < finish:
        if is_premium(current):
            ret.premium += 60
        else:
            ret.nonPremium += 60

        current = current + timedelta(minutes=60)

    return ret
