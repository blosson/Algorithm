board = [list(map(int, input().split())) for _ in range(5)]
called_number = [list(map(int, input().split())) for _ in range(5)]


for i in range(5):
    for j in range(5):
        number = called_number[i][j]

        for k in range(5):
            for l in range(5):
                if board[k][l] == number:
                    borad[k][l] = 0
        
        all_cnt = 0                     # 행, 열, 대각선(2개) 계속해서 검사해서 all_cnt == 3 나오면 출력
        cnt = 0
        for x in range(5):
            for y in range(5):
                if board[x][y] == 0:
                    cnt += 1
                    if cnt == 5:
                        all_cnt += 1



