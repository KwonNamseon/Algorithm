# 버블 정렬(Bubble Sort)
# 시간복잡도 O(n^2)
# 인접한 두 수를 비교하며 정렬해나가는 방법으로 O(n²)의 느린 성능을 가지고 있습니다.
# 앞에서부터 시작하여 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성해나가는 방법
# 또는 뒤에서부터 반복하여 앞의 작은 값부터 정렬을 완성해나가는 방법이 있습니다.


array = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)


print("before: ", array)
bubble_sort(array)
print("after:", array)
