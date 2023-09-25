import sys
sys.stdin = open('1979.txt', 'r')

for tc in range(1, int(input()) + 1):

    N, K = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(N))

    cnt_row = 0                             # 행 계산
    for i in range(N):
        for j in range(N-K+1):              # 길이가 K인 경우 N-K개 만큼 한 행에 들어갈 수 있음
            if board[i][j:j+K] == [1] * K:  # 슬라이싱해서 해당 구간이 [1] * K와 같으면 (모두 빈 자리면)
                if j == N - K:              # 제일 마지막 위치의 경우
                    if board[i][j-1] == 0:  # 바로 앞 index 값이 0이면 성공!
                        cnt_row += 1
                elif j == 0:                # 제일 처음 위치의 경우
                    if board[i][j+K] == 0:  # 바로 뒤 index 값이 0이면 성공!
                        cnt_row += 1
                else: 
                    if board[i][j+K] == 0 and board[i][j-1] == 0:   # 바로 앞, 뒤 모두 0이면 성공!
                        cnt_row += 1

# 열의 경우에는 슬라이싱이 안되므로 빈리스트에 append를 해주어 리스트 비교를 해주자!                        

    cnt_col = 0                             # 열 계산
    for j in range(N):
        for i in range(N-K+1):
            col_list = []                   
            for k in range(K):              # K번 만큼 슬라이싱처럼 빈 리스트에 넣어준다
                col_list.append(board[i+k][j])
            if col_list == [1] * K:
                if i == N - K:              # 제일 마지막 위치의 경우
                    if board[i-1][j] == 0:
                        cnt_col += 1
                elif i == 0:                # 제일 처음 위치의 경우
                    if board[i+K][j] == 0:
                        cnt_col += 1
                else: 
                    if board[i+K][j] == 0 and board[i-1][j] == 0:
                        cnt_col += 1


    ans = cnt_row + cnt_col
    print(f'#{tc} {ans}')


        
        