# 2581 소수

M = int(input())
N = int(input())

prime_numbers = []


def find_prime_number(number: int) -> bool:
    divisor_number = 0  # 약수 갯수
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_number += 1

    if divisor_number == 2:
        return True


for num in range(M, N + 1):
    if find_prime_number(num):
        prime_numbers.append(num)

if len(prime_numbers) > 0:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)
