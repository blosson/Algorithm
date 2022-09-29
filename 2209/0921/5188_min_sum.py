# 혼자 못 풀겠어서 다윗님 코드 클론코딩했습니다.. dfs다 까먹었는데 다시 복습해야겠네요.

delta = [[0, 1], [1, 0]]                                                # 델타 정의 / 오른쪽, 아래

def dfs(n, v):                                                          # dfs 함수 정의 / n: 칸의 인덱스, v: 현재까지 숫자 합
    global min_sum

    row, col = n
    now_sum = v + score[row][col]                                       # 현재 칸까지의 합
    if now_sum >= min_sum:                                              # 백트랙킹: 현재 칸까지의 합이 min_sum 이상일 경우
        return
    if row == board_size-1 and col == board_size-1:                     # 목적지 칸에 도달했으면 min_sum 갱신
        min_sum = now_sum
    else:
        for d in delta:
            if 0<=row+d[0]<board_size and 0<=col+d[1]<board_size:       # 델타만큼 이동하려는 칸이 유효한 칸일 경우,
                dfs([row+d[0], col+d[1]], now_sum)                      # 재귀 호출


tests = int(input())

for tc in range(1, tests+1):
    board_size = int(input())
    score = [list(map(int, input().split())) for _ in range(board_size)]

    min_sum = 13**2 * 10                                                # 13: N의 최대크기 / 10: 칸 숫자의 최대 크기
    dfs([0,0], 0)

    print(f'#{tc} {min_sum}')