# Modified Date

import os
import datetime
import time

#Current Date
current_timestamp = int(time.time())
print(f'Current Timestamp = {current_timestamp}\n')

#Current Date
dt_object_1 = datetime.datetime.fromtimestamp(current_timestamp)
print('Convert Current TimeStamp = ', end='')
print(dt_object_1.strftime('%Y-%m-%d %H:%M:%S'))
print("-----------------------------------------")

print('Input')
file_name = str(input('file_name = '))

file_path = file_name + '.txt'

print('Enter the date in the past you want to modified?')
print('[year, month, day, hour, minute, second]')
print('2023-9-11-20-11-10')
print('Date = ', end="")
input_past_time = str(input())
print("-----------------------------------------")

#print(type(input_past_time))
#print(input_past_time)

input_past_time_list = input_past_time.split('-')
#print(type(input_past_time_list))
#print(input_past_time_list)

year = input_past_time_list[0]
month = input_past_time_list[1]
day = input_past_time_list[2]
hour = input_past_time_list[3]
minute = input_past_time_list[4]
second = input_past_time_list[5]

print("-----------------------------------------")
print('Output')
print('Date = {}/{}/{}  Time = {}:{}:{}'.format(year, month, day, hour, minute, second))

#(year, month, day, hour, minute, second, microsecond, timezone, daylight, saving time)
modified_date = time.mktime((int(year), int(month), int(day), int(hour), int(minute), int(second), 0, 0, 0))
os.utime(file_path, (modified_date, modified_date))

print('!!!!!!!Done!!!!!!!')


#end