from time import sleep
from random import random, uniform
from datetime import datetime, timedelta

class random_timeout:
    '''Random timeout between from and to values'''
    def __init__(self, from_seconds=None, to_seconds=None, from_minutes=None, to_minutes=None, from_hours=None, to_hours=None, from_days=None, to_days=None):
        if from_seconds is not None:
            minimum = from_seconds
            if to_seconds:
                maximum = to_seconds
            else:
                maximum = minimum
        elif from_minutes is not None:
            minimum = from_minutes * 60
            if to_minutes:
                maximum = to_minutes * 60
            else:
                maximum = minimum
        elif from_hours is not None:
            minimum = from_hours * 3600
            if to_hours:
                maximum = to_hours * 3600
            else:
                maximum = minimum
        elif from_days is not None:
            minimum = from_days * 60
            if to_days:
                maximum = to_days * 86400
            else:
                maximum = minimum
        
        if minimum <= 0:
            minimum = random()
        else:
            minimum -= random() # Random float between 0 and 1
        maximum += random()
        timeout_in_seconds = uniform(minimum, maximum) # Random float between minimum and maximum
        if from_minutes or timeout_in_seconds > 60:
            timeout_in_minutes = round(timeout_in_seconds / 60) # Convert sleep time in seconds to minutes
            til = datetime.now() + timedelta(minutes=timeout_in_minutes)
            til = til.strftime('%H:%M')
            print('Sleeping', timeout_in_minutes, 'minutes until', til)
        elif from_hours or timeout_in_seconds > 3600:
            timeout_in_hours = round(timeout_in_seconds / 3600) # Convert sleep time in seconds to hours
            til = datetime.now() + timedelta(hours=timeout_in_hours)
            til = til.strftime('%H:%M')
            print('Sleeping', timeout_in_hours, 'hours until', til)
        elif from_days or timeout_in_seconds > 86400:
            timeout_in_hours = round(timeout_in_seconds / 86400) # Convert sleep time in seconds to days
            til = datetime.now() + timedelta(days=timeout_in_days)
            til = til.strftime('%A, %B %e')
            print('Sleeping', timeout_in_days, 'days until', til)
        sleep(timeout_in_seconds)

class sleep_for:
    '''Sleep amount of time in minutes, hours or days and prints when it will continue'''
    def __init__(self, minutes=None, hours=None, days=None):
        if minutes:
            til = datetime.now() + timedelta(minutes=minutes)
            til = til.strftime('%H:%M')
            print('Sleeping', minutes, 'minutes until', til)
            print()
            sleep(minutes * 60)
        elif hours:
            til = datetime.now() + timedelta(hours=hours)
            til = til.strftime('%H:%M')
            print('Sleeping', hours, 'hours until', til)
            print()
            sleep(hours * 3600)
        else:
            til = datetime.now() + timedelta(days=days)
            til = til.strftime('%A, %B %e')
            print('Sleeping', days, 'days until', til)
            print()
            sleep(days * 86400)