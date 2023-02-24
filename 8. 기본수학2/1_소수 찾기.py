# 1978 소수 찾기

N = int(input())
numbers = list(map(int, input().split()))


prime_count = 0  # 소수의 갯수
for num in numbers:
    divisor_number = 0  # 약수 갯수
    for i in range(1, num+1):
        if num % i == 0:
            divisor_number += 1
    if divisor_number == 2:
        prime_count += 1

print(prime_count)