# 2750 수 정렬하기

N = int(input())
array = [int(input()) for _ in range(N)]


# 버블 정렬 이용
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


sorted_array = bubble_sort(array)
for i in range(N):
    print(sorted_array[i])