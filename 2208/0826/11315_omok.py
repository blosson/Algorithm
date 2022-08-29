for tc in range(1, int(input()) + 1):

    N = int(input())
    board = [list(input()) for _ in range(N)]

    ans = 'NO'                          # 기본 정답 값. 오목이 완성되면 'YES'로 바꿀 예정
    cnt = 0
    for i in range(N):                  # 행 case
        for j in range(N):
            if board[i][j] == 'o':      # o면 1씩 추가하는 방식
                cnt += 1
                if cnt >= 5:            # 5 이상이면 정답으로 바꿈 (함수로 표현해서 return 하면 시간단축 가능할듯)
                    ans = 'YES'
                    break
            else:
                cnt = 0

    cnt = 0
    for j in range(N):                  # 열 case
        for i in range(N):
            if board[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
                    break
            else:
                cnt = 0

    dx = [-1, 1, 1, -1]                 # 대각선 case
    dy = [1, 1, -1, -1]                 # 대각선 delta (1시부터 시계방향으로)

    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):                  # 대각선 한 방향 먼저 탐색 index (0, 1, 2, 3) 순서로
                if board[i][j] != 'o':          # board[i][j]가 o가 아니면
                    cnt = 0                     # cnt = 0으로 그대로 하고 break     
                    break                       # (자기자신이 o가 아니면 오목이 안 생기기 때문)
                else:
                    cnt = 1                     # board[i][j]가 o면
                    for l in range(1, 5):       # 자기자신 제외한 다음 4칸을 돌면서 delta값 더해주기
                        di = i + dx[k] * l      
                        dj = j + dy[k] * l
                        if 0 <= di < N and 0 <= dj < N and board[di][dj] == 'o': # 델타를 더한 인덱스가 범위 안에 있고 o값을 가지면
                            cnt += 1                                             # cnt 추가
                            if cnt >= 5:
                                ans = 'YES'
                                break
                        else:
                            cnt = 0
                    

    print(f'#{tc} {ans}')