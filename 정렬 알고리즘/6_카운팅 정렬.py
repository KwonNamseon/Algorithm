# 카운팅 정렬(Counting Sort)
# 시간복잡도 O(n)
# 데이터 수가 많더라도 중복된 값이 많이 분포돼있는 배열을 정렬할 때 효과적이고 빠른 정렬 알고리즘이다.
# 최대, 최소 값 차이가 100만 이하일 경우 효과적이다.

# 조건
# 데이터의 크기 범위가 제한된 경우(0 ~ 100)
# 데이터가 양의 정수인 경우
# 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000(백만)을 넘지 않는 경우

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def counting_sort(arr):
    max_arr = max(arr)
    count = [0] * (max_arr + 1)
    sorted_arr = list()

    for i in arr:  # 카운팅
        count[i] += 1

    for i in range(max_arr + 1):
        for _ in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr


print("before: ", array)
array = counting_sort(array)
print("after:", array)
