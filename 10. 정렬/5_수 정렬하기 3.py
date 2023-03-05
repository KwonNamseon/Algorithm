# 10989 수 정렬하기 3

# 카운팅 정렬
import sys

N = int(sys.stdin.readline())
count = [0] * (10000 + 1)

for _ in range(N):
    number = int(sys.stdin.readline())
    count[number] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
