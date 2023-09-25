N, M = map(int, input().split())
board = list(input() for _ in range(N))

# 비교 기준이 될 보드판 (흰색, 검은색 각각)
white = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']   
black = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

min_cnt = float('inf')                                  # 무한히 큰 수 (정답 변수)
for i in range(N-7):                                    # 순회할 범위 지정 (행, 열 모두 자신의 인덱스 포함 8만큼 길이가 있어야 함)
    for j in range(M-7):
        blank_board = []                                # 순회하면서 생성할 리스트
        for k in range(i, i+8):                         # 8*8 체스판 떼어내기
            blank_board.append(board[k][j:j+8])

        white_cnt = 0                                   # 흰색 보드판 체크 변수
        black_cnt = 0                                   # 검은색 보드판 체크 변수
        for x in range(8):                              # 순회하면서 각 인덱스 값이 다른 만큼 흰, 검 cnt 변수에 +1을 해줌
            for y in range(8):
                if blank_board[x][y] != white[x][y]:
                    white_cnt += 1
                
                if blank_board[x][y] != black[x][y]:
                    black_cnt += 1

        min_wb = min(white_cnt, black_cnt)              # 둘 중 최솟값 구해서 min_cnt와 비교한 후 더 작으면 바꿔줌
        if min_wb < min_cnt:
            min_cnt = min_wb 

print(min_cnt)
                
