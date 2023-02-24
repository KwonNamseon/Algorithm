# 1316 그룹 단어 체커

N = int(input())
count = 0

for i in range(1, N+1):
    word = input()
    result = ''
    is_group_word = True
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            result += word[j]
        if j == len(word) - 2:
            result += word[j + 1]

    for r in result:
        if result.count(r) > 1:
            is_group_word = False
            break

    if is_group_word:
        count += 1

print(count)
