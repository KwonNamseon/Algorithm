# 1065 한수

N = int(input())
count = 0


def find_numbers(number):
    numbers = list(map(int, str(number)))
    if number < 100:
        return True
    if numbers[1] - numbers[0] == numbers[2] - numbers[1]:
        return True
    return False


for num in range(1, N+1):
    if find_numbers(num):
        count += 1

print(count)

