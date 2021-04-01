import datetime


def pendulum_to_datetime(pendulum):
    dt_time = datetime.datetime(pendulum.year, pendulum.month, pendulum.day, pendulum.hour, pendulum.minute,
                                pendulum.second, pendulum.microsecond, pendulum.timezone)
    return dt_time
