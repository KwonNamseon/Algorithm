# 2884 알람 시계
hour, minutes = map(int, input().split())
second = hour * 3600 + minutes * 60
ealryTime = 45 * 60
alarmTime = second - ealryTime
if alarmTime < 0:
    alarmTime = 24 * 60 * 60 + alarmTime
alarmHour = alarmTime // 3600
alarmMinutes = (alarmTime % 3600) // 60
print(alarmHour, end=" ")
print(alarmMinutes)
