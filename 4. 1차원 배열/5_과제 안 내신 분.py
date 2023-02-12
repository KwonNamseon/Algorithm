# 5597 과제 안내신 분..?
import sys

array = list(range(1, 31))
for i in range(28):
    num = int(sys.stdin.readline())
    array.remove(num)

print(array[0])
print(array[1])