# 2599 곱셈
A = int(input())
B = int(input())
hundreds, tens, ones = map(int, str(B))
print(A * ones)
print(A * tens)
print(A * hundreds)
print(A * B)