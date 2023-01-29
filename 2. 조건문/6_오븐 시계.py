# 2525 오븐 시계
hour, minutes = map(int, input().split())
cookingTime = int(input()) * 60

second = hour * 3600 + minutes * 60
cookedTime = second + cookingTime # 초(s) 단위

if cookedTime >= 24 * 3600:
    cookedTime -= 24 * 3600

cookedHour = cookedTime // 3600
cookedMinutes = (cookedTime % 3600) // 60
print(cookedHour, end=" ")
print(cookedMinutes)
