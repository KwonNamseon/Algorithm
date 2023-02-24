# 2292 벌집

N = int(input())
count = 1
num = 1
while True:
    if num >= N:
        break
    num += 6 * count
    count += 1

print(count)