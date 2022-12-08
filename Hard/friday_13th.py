#%%

#https://edabit.com/challenge/Xkc2iAjwCap2z9N5D

import datetime as dt

def has_friday_13(month, year):
    return dt.datetime(year, month, 13).weekday() == 4

