# 2908 상수

A, B = map(list, input().split())
reverse_A = ''.join(reversed(A))
reverse_B = ''.join(reversed(B))

if reverse_A < reverse_B:
    print(reverse_B)
else:
    print(reverse_A)