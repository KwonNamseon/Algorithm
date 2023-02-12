# 4344 평균은 넘겠지
import sys

C = int(input())
for i in range(C):
    array = list(map(int, sys.stdin.readline().split()))
    average = sum(array[1:]) / array[0]
    count = 0
    for score in array[1:]:
        if score > average:
            count += 1
    print(f'{count / array[0] * 100:.3f}%')
