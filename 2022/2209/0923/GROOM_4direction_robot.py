n, m, k = map(int, input().split())
k = input()

delta = [[0, -1], [0, 1], [1, 0], [-1, 0]]      # 서동남북
star = [[0] * m for _ in range(n)]
star[0][0] = 1

di, dj = 0, 0
for i in k:
    if i == 'E':                    # 사실이게 서쪽임... 출제자 좀 혼나야할듯
        if di + delta[0][0] < 0 or di + delta[0][0] >= n or dj + delta[0][1] < 0 or dj + delta[0][1] >= m:  # 다음이 범위 바깥으로 가면
            star[di][dj] += 1       # 위치는 그대로 두고 해당 인덱스 값 + 1
        else:                       # 별 밖으로 안 나가면
            di += delta[0][0]       # di, dj 업데이트 해주고 방문 횟수 +1
            dj += delta[0][1]
            star[di][dj] += 1

    elif i == 'W':
        if di + delta[1][0] < 0 or di + delta[1][0] >= n or dj + delta[1][1] < 0 or dj + delta[1][1] >= m:
            star[di][dj] += 1

        else:
            di += delta[1][0]
            dj += delta[1][1]
            star[di][dj] += 1

    elif i == 'S':
        if di + delta[2][0] < 0 or di + delta[2][0] >= n or dj + delta[2][1] < 0 or dj + delta[2][1] >= m:
           star[di][dj] += 1 
        
        else:
            di += delta[2][0]
            dj += delta[2][1]
            star[di][dj] += 1

    else:
        if di + delta[3][0] < 0 or di + delta[3][0] >= n or dj + delta[3][1] < 0 or dj + delta[3][1] >= m:
               star[di][dj] += 1 
    
        else:
            di += delta[3][0]
            dj += delta[3][1]
            star[di][dj] += 1

ans = 0                         # 정답 (최다 방문 횟수)
for i in star:                  # 이중 리스트 순회
    star_max = max(i)           # 각 줄에서 가장 큰 값 구하기
    if star_max > ans:          # 최댓값보다 크면 업데이트
        ans = star_max

print(ans)