from datetime import datetime, time, timedelta

import pymongo
import streamlit as st


# Get time untill sunday 20:00
def get_timer():
    today = datetime.today()
    t = datetime.combine(today.date() + timedelta((6 - today.weekday()) % 7), time(20))
    if today > t:
        t += timedelta(7)
    delta = t - today
    totalSeconds = delta.total_seconds()
    days, left = divmod(totalSeconds, 86400)
    hours, remainder = divmod(left, 3600)
    minutes, seconds = divmod(remainder, 60)

    return int(days), int(hours), int(minutes)
