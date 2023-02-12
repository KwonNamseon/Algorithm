# 3052 나머지
import sys

N = 10
result = []
for i in range(N):
    A = int(sys.stdin.readline())
    B = 42
    result.append(A % B)

print(len(set(result)))
