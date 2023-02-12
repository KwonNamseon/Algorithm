# 2562 최댓값
import sys

result = 0
index = 0
for i in range(9):
    num = int(sys.stdin.readline())
    if num > result:
        result = num
        index = i

print(result)
print(index + 1)