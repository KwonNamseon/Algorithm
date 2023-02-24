# 1929 소수 구하기

# 2581 소수

M, N = map(int, input().split())

# 에라토스테네스의 체
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:  # 약수 존재
            break
    else:
        print(i)