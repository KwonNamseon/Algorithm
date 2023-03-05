# 2108 통계학
import sys
from collections import Counter

N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(N)]
array.sort()  # 정렬을 시킨 후 계산

# 산술 평균
mean = round(sum(array) / N)
print(mean)

# 중앙값
median = array[N // 2]
print(median)

# 최빈값
# count 함수 시간초과 => Collection 라이브러리의 Counter 함수 사용
max_count = 0
modes = Counter(array).most_common()
if len(modes) > 1 and modes[0][1] == modes[1][1]:
    # 최빈값이 여러개인 경우 두번째로 작은 값 출력
    print(modes[1][0])
else:
    print(modes[0][0])

# 범위
min_number = min(array)
max_number = max(array)
range_array = max_number - min_number
print(range_array)
