# 2525 오븐 시계
hour, minutes = map(int, input().split())
cooking_time = int(input()) * 60

second = hour * 3600 + minutes * 60
cooked_time = second + cooking_time # 초(s) 단위

if cooked_time >= 24 * 3600:
    cooked_time -= 24 * 3600

cooked_hour = cooked_time // 3600
cooked_minutes = (cooked_time % 3600) // 60
print(cooked_hour, end=" ")
print(cooked_minutes)
