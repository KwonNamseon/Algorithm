# 삽입 정렬(Insertion Sort)
# 시간복잡도 : O(n^2)
# 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
# 버블 정렬과 선택 정렬과 마찬가지로 최악의 성능인 정렬 알고리즘입니다.

array = [8, 4, 6, 2, 9, 1, 3, 7, 5]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, - 1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
        print(array[:i+1])

print("before: ", array)
insertion_sort(array)
print("after:", array)
