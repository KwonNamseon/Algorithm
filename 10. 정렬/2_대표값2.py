# 2587 대표값2

# 선택 정렬(Selection Sort)
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


N = 5
numbers = [int(input()) for _ in range(N)]

average = sum(numbers) // N  # 평균
sorted_numbers = selection_sort(numbers)
middle_number = sorted_numbers[2]  # 중앙값

print(average)
print(middle_number)
