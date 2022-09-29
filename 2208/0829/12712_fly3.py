delta_plus_i = [0, 1, 0 ,-1]    # +방향 델타
delta_plus_j = [1, 0, -1, 0]
delta_x_i = [-1, 1, 1, -1]      # x방향 델타
delta_x_j = [1, 1, -1, -1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_ans = 0                             # 정답
    for i in range(N):
        for j in range(N):
            max_plus = board[i][j]          # 중앙값은 고정으로 넣어줌
            max_x = board[i][j]
            for k in range(1, M):           # 중앙값을 넣어줬으니 range(1, ~~)로 시작
                for l in range(4):          # 델타 이동
                    plus_ni, plus_nj = (i + (k * delta_plus_i[l])), (j + (k * delta_plus_j[l]))     # K, l, M 변수 착각 주의
                    x_ni, x_nj = (i + (k * delta_x_i[l])), (j + (k * delta_x_j[l]))

                    if 0 <= plus_ni < N and 0 <= plus_nj < N:     # index 벗어나는 경우가 있으므로 반드시 조건 주기
                        max_plus += board[plus_ni][plus_nj]
                    if 0 <= x_ni < N and 0 <= x_nj < N:
                        max_x += board[x_ni][x_nj]
            max_value = max(max_plus, max_x)                      # +와 x 중 더 큰 값 선택
            if max_value > max_ans:
                max_ans = max_value
    
    print(f'#{tc} {max_ans}')


            