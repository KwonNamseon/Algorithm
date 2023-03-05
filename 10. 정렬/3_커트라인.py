# 25305 커트라인

# 삽입 정렬(Insertion Sort)
# 가장 큰 수가 앞으로 가도록 수정
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, - 1):
            if array[j - 1] < array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


N, K = map(int, input().split())
scores = list(map(int, input().split()))

sorted_scores = insertion_sort(scores)
print(sorted_scores[K - 1])
