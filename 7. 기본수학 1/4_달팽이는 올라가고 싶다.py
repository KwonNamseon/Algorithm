# 2869 달팽이는 올라가고 싶다
import math

A, B, V = map(int, input().split())

# 공식 Ax + B(x-1) >= V
print(math.ceil((V - B) / (A - B)))
