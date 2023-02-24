# 9020 골드바흐의 추측

# 1 ~ 10000까지의 소수 구하기
prime_numbers = []
for i in range(1, 10000+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:  # 약수 존재
            break
    else:
        prime_numbers.append(i)

T = int(input())
for _ in range(T):
    N = int(input())
    X = 0
    Y = 0
    for num in prime_numbers:
        if num > N // 2:
            break
        if N - num in prime_numbers:
            X = num
            Y = N - num

    print(f'{X} {Y}')
