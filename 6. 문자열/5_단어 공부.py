# 1157 단어 공부
import sys

alphabel = 'abcdefghijklmnopqrstuvwxyz'.upper()
S = sys.stdin.readline()
S = S.upper()
result = ''
max_count = 0

for a in alphabel:
    if max_count < S.count(a):
        max_count = S.count(a)
        result = a
    elif max_count != 0 and max_count == S.count(a):
        result = '?'

print(result)
