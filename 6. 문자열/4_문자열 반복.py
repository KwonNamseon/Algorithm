# 2675 문자열 반복

T = int(input())

for t in range(1, T+1):
    C = list(map(str, input().split()))
    R, S = int(C[0]), C[1]
    result = ''

    for s in S:
        result += (s * R)

    print(result)