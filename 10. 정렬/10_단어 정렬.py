# 1181 단어 정렬
import sys

N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]
filtered_words = list(set(words))
filtered_words.sort(key=lambda x: (len(x), x))

for word in filtered_words:
    print(word)
