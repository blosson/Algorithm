# 왜 시간초과 나냐고...

N, M = map(int, input().split())
pocketmon = [0] * (N+1)                     # 포켓몬 도감 만들기 (1번부터 시작하므로 N+1)
for i in range(N):                          # 포켓몬 도감에 idx와 이름 함께 저장해주기
    pocketmon[i+1] = (i+1, input())

# print(pocketmon)

for i in range(M):                          # 맞춰야 하는 문제의 갯수
    who = input()
    # print('hi', who.isdecimal())          # 숫자 형태, 문자 형태 구분해주기

    if who.isdecimal():                     # 포켓몬 번호면
        ans = pocketmon[int(who)][1]        # 포켓몬 이름을 ans에 저장

    else:                                   # 포켓몬 이름이면
        for i in range(N):                  # 포켓몬 번호를 저장
            if pocketmon[i+1][1] == who:
                ans = pocketmon[i+1][0]

    
    print(ans)                              # 정답 출력