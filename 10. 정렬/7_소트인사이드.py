# 1427 소트인사이드
import sys

numbers = [int(num) for num in sys.stdin.readline().strip()]
# 내림차순 정렬 sort 함수의 default는 오름차순(reverse=True)
numbers.sort(reverse=True)
print(''.join(map(str, numbers)))

