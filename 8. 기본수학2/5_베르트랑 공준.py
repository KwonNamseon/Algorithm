# 4948 베르트랑 공준

def find_prime_number(m: int, n: int) -> int:
    count = 0
    for i in range(m, n + 1):
        if i == 1:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:  # 약수 존재
                break
        else:
            count += 1

    return count


while True:
    N = int(input())
    if N == 0:
        break
    print(find_prime_number(N + 1, N * 2))
