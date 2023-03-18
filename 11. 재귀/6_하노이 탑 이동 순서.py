# 11729 하노이 탑 이동 순서

def hanoi(start: int, end: int, n: int):
    if n == 0:
        return

    # n-1개의 원판을 2번 위치로 옮긴다.
    hanoi(start, 6 - start - end, n - 1)
    # n번 원판을 3번 위치로 옮긴다.
    print(start, end)
    # n-1개의 원판을 3번 위치로 옮긴다.
    hanoi(6 - start - end, end, n - 1)


N = int(input())
count = 0
print(2**N - 1)
hanoi(1, 3, N)
if 