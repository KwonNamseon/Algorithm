# 11651 좌표 정렬하기2

# 11650 좌표 정렬하기

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
# 정렬 조건
# 첫번째 조건 : y 좌표 오름차순
# 두번째 조건 : x 좌표 오름차순
# array.sort()과 동일한 결과 출력됨
array.sort(key=lambda x: (x[1], x[0]))

for numbers in array:
    for num in numbers:
        print(num, end=' ')
    print()
