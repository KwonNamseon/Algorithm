# 10798 세로읽기

import sys

words = []
for _ in range(5):
    word = sys.stdin.readline().strip()
    word += '*' * (15 - len(word))
    words.append(word)

for i in range(15):
    for j in range(len(words)):
        if words[j][i] == '*':
            continue
        print(words[j][i], end='')

