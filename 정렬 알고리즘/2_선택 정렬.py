# 선택 정렬(Selection Sort)
# 시간복잡도 : O(n^2)
# 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬.
# 앞에서부터 정렬해나가는 특성을 가지고 있고 버블 정렬과 마찬가지로 최악의 성능을 가진 알고리즘입니다.

array = [8, 4, 6, 2, 9, 1, 3, 7, 5]


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(array[:i+1])


print("before: ", array)
selection_sort(array)
print("after:", array)
