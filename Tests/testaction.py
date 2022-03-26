from Action import Action

date_string1 = "2022-01-23"
date_string2 = "2019-04-14"
time_string1 = "17:00:01-0700"
time_string2 = "12:32:16-0700"
date_time1_string = '2022-01-23 17:00:01-07:00'
date_time2_string = '2019-04-14 12:32:16-07:00'

action = Action(None, "My Action", "Action Long", date_string2, time_string2, date_string1, time_string1)

print(action.start_date)
print(action.end_date)
print(action.start_date_time)
print(action.end_date_time)
print(action.duration_string)
print(action.action_time_span)
# 2019-04-14
# 2022-01-23
# 2019-04-14 12:32:16-07:00
# 2022-01-23 17:00:01-07:00
# 1015 days, 4 hours, 27 minutes, 45 seconds
# Start: 2019-04-14 12:32:16-07:00
# End: 2022-01-23 17:00:01-07:00
# Duration: 1015 days, 4 hours, 27 minutes, 45 seconds

# bump start date by 1
action.start_date = "2019-04-15"
print(action.start_date)
print(action.end_date)
print(action.start_date_time)
print(action.end_date_time)
print(action.duration_string)
print(action.action_time_span)
# 2019-04-15
# 2022-01-23
# 2019-04-15 12:32:16-07:00
# 2022-01-23 17:00:01-07:00
# 1014 days, 4 hours, 27 minutes, 45 seconds
# Start: 2019-04-15 12:32:16-07:00
# End: 2022-01-23 17:00:01-07:00
# Duration: 1014 days, 4 hours, 27 minutes, 45 seconds