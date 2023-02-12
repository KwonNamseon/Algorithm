# 1546 평균
import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
max_score = max(scores)
new_scores = []

for score in scores:
    new_scores.append(score / max_score * 100)

print(sum(new_scores) / N)