# 2941 크로아티아 알파벳
import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = sys.stdin.readline().strip()

for c in croatia:
    S = S.replace(c, 'c')

print(len(S))