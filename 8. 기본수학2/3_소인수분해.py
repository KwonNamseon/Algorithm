# 11653 소인수분해

N = int(input())

divider = 2
while N > 1:
    if N % divider == 0:
        print(divider)
        N = N // divider
    else:
        divider += 1

