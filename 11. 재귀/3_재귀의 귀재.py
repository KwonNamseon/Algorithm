# 25501 재귀의 귀재
import sys


def recursion(word: str, left: int, right: int) -> int:
    global count
    count += 1
    if left >= right:
        return 1
    elif word[left] != word[right]:
        return 0
    return recursion(word, left + 1, right - 1)


def is_palindrome(word: str) -> int:
    return recursion(word, 0, len(word) - 1)


N = int(input())
for _ in range(N):
    word = sys.stdin.readline().strip()
    count = 0
    print(is_palindrome(word), count)
