# 1110 더하기 사이클
N = int(input())
count = 0  # 사이클 수
sum_of_num = 0  # 각 자리 수의 합
new_num = N  # 새로운 수
while 1:
    if new_num == N and count != 0:
        print(count)
        break
    else:
        sum_of_num = new_num // 10 + new_num % 10
        new_num = (new_num % 10) * 10 + (sum_of_num % 10)
        count += 1
