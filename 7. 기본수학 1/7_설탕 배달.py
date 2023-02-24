# 2839 설탕 배달

N = int(input())

X = N // 5  # 5kg 최대 갯수
result = 0
for x in range(X, -1, -1):
    if (N - x * 5) % 3 == 0:
        y = (N - x * 5) // 3
        result = x + y
        break

if result == 0:
    print(-1)
else:
    print(result)
