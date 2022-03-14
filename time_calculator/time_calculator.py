# This entrypoint file to be used in development. Start by reading README.md
#from time_calculator import add_time
#from unittest import main

import datetime

def add_time(start, duration, *args):
    daysofTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysofTheWeek_scan = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    pm_add_sec = 60 * 60 * 12
    day_index = 0

    for argument in args:        
        day_index = daysofTheWeek_scan.index(argument.lower())
        #print(argument.lower(), day_index)
    
    ##### convert parameters into seconds
    # process start Parameter , convert to seconds
    start_splt = start.split(":")    
    start_hours_sec = int(start_splt[0]) * seconds_in_hour
    am_pm_splt = (start_splt[1]).split(" ")
    start_minute_sec = int(am_pm_splt[0]) * seconds_in_minute
    am_pm = am_pm_splt[1]
    added_start_time = start_hours_sec + start_minute_sec

    # Add 12 hours for PM
    if am_pm == 'PM':
        added_start_time = added_start_time + pm_add_sec

    # process duration Parameter, convert to seconds
    duration_splt = duration.split(":")    
    duration_hours_sec = int(duration_splt[0]) * seconds_in_hour
    duration_minute_sec = int(duration_splt[1]) * seconds_in_minute
    added_duration_time = duration_hours_sec + duration_minute_sec
    
    # Add duration and start
    added_time = added_start_time + added_duration_time
    
    # Convert back to Day Hour Minute 
    days = added_time // seconds_in_day
    
    added_time %= seconds_in_day
    hours = added_time // seconds_in_hour
 
    added_time %= seconds_in_hour
    minutes = added_time // seconds_in_minute

    #Return values
    if hours < 12:
        tod = 'AM'
        if hours == 0:
            hours = 12
    else:
        tod = 'PM'


    return_str = ''
    return_day = 'Monday'
    return_day_later = ' (next day)'    
    return_days_later = ' (' + str(days) + ' days later)'
    
    #return_HM_tod = f'{hours:02d}' + ':'+ f'{minutes:02d}' + ' ' + tod
    if tod == 'PM' and hours > 12:
        hours = hours - 12

    return_HM_tod = f'{hours:01d}' + ':'+ f'{minutes:02d}' + ' ' + tod

    if args:
            #lookup day
        next_day_index = day_index + days
        if next_day_index > 5:
                #next_day_index_1 = next_day_index % 6
            next_day_index = next_day_index % 7

        return_day = daysofTheWeek[next_day_index] 
        return_day_str = ', ' + return_day

    if days >= 2:

        if args:
            #lookup day
            next_day_index = day_index + days
            if next_day_index > 5:
                #next_day_index_1 = next_day_index % 6
                next_day_index = next_day_index % 7

            return_day = daysofTheWeek[next_day_index] 
            return_day_str = ', ' + return_day
            return_str = return_HM_tod + return_day_str + return_days_later
        else:
            return_str = return_HM_tod + return_days_later
        
    elif not args and days == 1:
        return_str = return_HM_tod + return_day_later

    elif args and days == 0:
        return_str = return_HM_tod + return_day_str

    elif args and days == 1:
        return_str = return_HM_tod + return_day_str + return_day_later

    else:    
        return_str = return_HM_tod 
    
    return return_str

#print(add_time("2:59 AM", "24:00", "saturDay"))
#"2:59 AM, Sunday (next day)"

#print(add_time("8:16 PM", "466:02", "tuesday"))
#"6:18 AM, Monday (20 days later)"

#print(add_time("11:55 AM", "3:12"))
#"3:07 PM"

#print(add_time("3:30 PM", "2:12", "Monday"))
#"5:42 PM, Monday"