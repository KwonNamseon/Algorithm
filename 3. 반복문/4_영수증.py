# 25304 영수증
X = int(input())
N = int(input())
result = 0
for i in range(0, N):
    a, b = map(int, input().split())
    result += (a * b)

if X == result:
    print('Yes')
else:
    print('No')