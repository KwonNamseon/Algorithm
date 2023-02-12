# 10807 개수 세기
import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
v = int(input())

result = 0
for i in range(N):
    if array[i] == v:
        result += 1

print(result)