# 10814 나이순 정렬
import sys

N = int(input())
user_list = [list(sys.stdin.readline().strip().split()) for _ in range(N)]
user_list.sort(key=lambda x: (int(x[0])))

for user in user_list:
    print(' '.join(user))