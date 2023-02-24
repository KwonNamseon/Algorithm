# 5622 다이얼
import sys

alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = sys.stdin.readline()

result = 0  # 최소 시간
for s in S:
    for index, a in enumerate(alphabet):
        if s in a:
            result += index + 3 # 알파벳에 맞는 숫자(index + 1) + 2

print(result)