# 뒤에 공백 있는 ver (화면상은 똑같으나 정답 인정 안됨)

N = int(input())

for i in range(1, N + 1):
    blank_list = [' '] * (2 * N - 1)  # N에 따른 리스트 생성  
    blank_list[N - i] = '*'           # 앞쪽 규칙
    blank_list[i - N - 1] = '*'       # 뒷쪽 규칙 - i == 1의 경우 N-i == i - N - 1 (즉, 중복 됨)
    print(*blank_list)


# 뒤에 공백 없는 ver

N = int(input())

for i in range(1, N + 1):
    blank_list = [' '] * (2 * N - 1)  # N에 따른 리스트 생성  
    blank_list[N - i] = '*'           # 앞쪽 규칙
    blank_list[i - N - 1] = '*'       # 뒷쪽 규칙 - i == 1의 경우 N-i == i - N - 1 (즉, 중복 됨)
    blank_str = ''
    for blank in blank_list:
        blank_str += blank
    ans = blank_str.rstrip()
    print(ans)
    




