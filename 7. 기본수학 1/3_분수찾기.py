# 1193 분수찾기

N = int(input())

line = 0  # 대각선 라인
end = 0  # 대각선 마지막 숫자
while N > end:
    line += 1
    end += line

index = end - N  # 대각선에서 몇번째 index
if line % 2:
    # 짝수 라인의 경우 분자는 1씩 증가, 분모는 1씩 감소
    print(f'{index + 1}/{line - index}')
else:
    # 홀수 라인의 경우 분자는 1씩 감소, 분모는 1씩 증가
    print(f'{line - index}/{index + 1}')
