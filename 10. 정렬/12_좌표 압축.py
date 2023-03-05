# 18870 좌표 압축
import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
# 시간초과
# sorted, sort 시간복잡도 O(nlogn)
# dictionary 시간복잡도 O(1)
sorted_array = sorted(set(array))
dictionary = {sorted_array[i]: i for i in range(len(sorted_array))}

for num in array:
    print(dictionary[num], end=' ')

