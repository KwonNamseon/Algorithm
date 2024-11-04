# 23971 ZOAC 4

# def get_count_step(length, step):
#     count = 0
#     for i in range(1, length, step):
#         count += 1
#
#     return count
#
# H, W, N, M = map(int, input().split())
# row_count = get_count_step(W+1, M+1)
# column_count = get_count_step(H+1, N+1)
#
# print(row_count * column_count)

# 간단한 풀이
H, W, N, M = map(int, input().split())

# 자기 자신을 포함해 거리두기 규칙에 맞게 앉을 수 있는 좌석 수 계산
row_count = (W + M) // (M + 1)
column_count = (H + N) // (N + 1)

print(row_count * column_count)