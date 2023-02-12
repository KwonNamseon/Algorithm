# 8958 OX퀴즈
import sys

N = int(input())
for i in range(N):
    array = list(sys.stdin.readline().strip())
    count = 0
    score = 0
    for j in array:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)