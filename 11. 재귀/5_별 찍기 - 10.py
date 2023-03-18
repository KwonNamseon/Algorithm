# 2447 별 찍기 - 10

def draw_star(n: int) -> list:
    if n == 1:
        return ['*']
    stars = draw_star(n // 3)
    result = []
    for i in range(3):
        for star in stars:
            if i == 1:  # 가운데 줄만 다르게 계산
                result.append(star + ' ' * (n // 3) + star)
            else:
                result.append(star * 3)

    return result


N = int(input())
for star in draw_star(N):
    print(star)

