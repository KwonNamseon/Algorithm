# 2566 최댓값

array = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
row = 1
column = 1

for i in range(9):
    for j in range(9):
        if array[i][j] > max_num:
            max_num = array[i][j]
            row = i + 1
            column = j + 1

print(max_num)
print(row, column)
