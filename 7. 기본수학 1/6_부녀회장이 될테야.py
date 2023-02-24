# 2775 부녀회장이 될테야

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    zero_floor = [i for i in range(1, n+1)]
    apartment = [zero_floor]  # 0층 ~ k층
    for i in range(k):
        floor = []
        for j in range(n):
            floor.append(sum(apartment[i][:j+1]))
        apartment.append(floor)
    print(apartment[k][n-1])
