# BOJ_10798 세로읽기 (B1)

letters = []
for i in range(5):
    letters.append(input())

# 각 str의 길이를 배열에 저장
len_list = []
for i in range(5):
    len_list.append(len(letters[i]))

# 첫 for문의 range 범위를 정하기 위해 최대 문자열 길이를 변수에 저장
max_len = max(len_list)

ans = []
for i in range(max_len):
    for j in range(5):
        # 해당 행의 str 길이가 i+1과 같거나 크면 정답 list에 append
        if len_list[j] >= i+1:
            ans.append(letters[j][i])        

print(*ans, sep="")