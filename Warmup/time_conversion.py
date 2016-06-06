#!/bin/python3

import sys


time = input().strip()

def time_converter(time):
    time = str(time)
    hr = int(time[:2])
    part_of_day = time[-2:]
    if part_of_day == 'AM' and 1 <= hr <= 11:
        print(time[:-2])
    elif part_of_day == 'PM' and hr == 12:
        print(time[:-2])
    elif part_of_day == 'PM' and 1 <= hr <= 11:
        print(str(hr + 12) + time[2:-2])
    elif part_of_day == 'AM' and hr == 12:
        print('00' + time[2:-2])

time_converter(time)