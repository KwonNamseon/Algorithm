# 24060 알고리즘 수업 - 병합 정렬 1

# 예시 [4, 5, 1, 3, 2]
# 분할
#                           middle = 3,
#       left = [4, 5, 1],                     right = [3, 2]
#           middle = 2                          middle = 1
#   left = [4, 5], right = [1]            left = [3], right = [2]
#     middle = 1
# left: [4], right[5]

# 병합
#               [1, 4, 5] * [2, 3] => [1, 2, 3, 4, 5]
#   [4, 5] * [1] => [1, 4, 5]           [3] * [2] => [2, 3]
#       [4] * [5] => [4, 5]

def merge_sort(array):
    global result

    if len(array) < 2:
        return array

    middle = (len(array) + 1) // 2  # 중간을 나눌때 앞이 크도록 병합
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    merged_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            result.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            result.append(right[j])
            j += 1
    while i < len(left):
        merged_arr.append(left[i])
        result.append(left[i])
        i += 1
    while j < len(right):
        merged_arr.append(right[j])
        result.append(right[j])
        j += 1

    return merged_arr


N, K = map(int, input().split())
array = list(map(int, input().split()))
result = []
merge_sort(array)

if len(result) < K:
    print(-1)
else:
    print(result[K - 1])


