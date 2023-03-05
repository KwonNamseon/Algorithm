# 2562 색종이

def attach_paper(row, column):
    global paper
    for i in range(M):
        for j in range(M):
            if row <= i < row + 10 and column <= j < column + 10:
                paper[i][j] += 1
    return paper


M = 100  # 도화지 크기 100 x 100
N = int(input())
paper = [[0]*M for _ in range(M)]
for _ in range(N):
    row, column = map(int, input().split())
    attach_paper(row - 1, column - 1)

# paper 출력

count = 0
for i in range(M):
    for j in range(M):
        if paper[i][j] != 0:
            count += 1

print(count)
