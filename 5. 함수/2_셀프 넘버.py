# 4673 셀프 넘버

numbers = list(range(1, 10001))
no_self_numbers = set()


def find_numbers(number):
    numbers = number
    for num in str(number):
        numbers += int(num)
    return numbers


for n in numbers:
    result = find_numbers(n)
    if 0 < result <= 10000:
        no_self_numbers.add(result)

for n in sorted(no_self_numbers):
    numbers.remove(n)

print(*numbers, sep='\n')
