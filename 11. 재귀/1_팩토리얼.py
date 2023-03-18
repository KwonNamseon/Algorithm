# 10872 팩토리얼

def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n - 1)


N = int(input())

print(factorial(N))
