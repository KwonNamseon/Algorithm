# 10870 피보나치 수 5

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


N = int(input())

print(fibonacci(N))  # 초기값 0, 1 지정
