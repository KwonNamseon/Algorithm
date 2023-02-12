# 10818 최소, 최대
import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
min = 1000000
max = -1000000
for i in range(N):
    if array[i] < min:
        min = array[i]
    if array[i] > max:
        max = array[i]

print(f'{min} {max}')