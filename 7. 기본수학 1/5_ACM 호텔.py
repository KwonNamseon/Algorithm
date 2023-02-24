# 10250 ACM 호텔

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        X = N // H
        Y = H
    else:
        X = N // H + 1
        Y = N % H

    if X < 10:
        print(f'{Y}0{X}')
    else:
        print(f'{Y}{X}')



