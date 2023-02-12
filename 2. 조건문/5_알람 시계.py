# 2884 알람 시계
hour, minutes = map(int, input().split())
second = hour * 3600 + minutes * 60
ealry_time = 45 * 60
alarm_time = second - ealry_time
if alarm_time < 0:
    alarm_time = 24 * 60 * 60 + alarm_time
alarm_hour = alarm_time // 3600
alarm_minutes = (alarm_time % 3600) // 60
print(alarm_hour, end=" ")
print(alarm_minutes)
