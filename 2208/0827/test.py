for tc in range(1, int(input()) + 1):
    
    N = int(input())
    board = [list(input()) for _ in range(N)]

    ans = 'no'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                cnt += 1


    def find_ij(board):
        i1 = j1 = -1
        for i in range(N):
            for j in range(N):
                if board[i][j] == '#':
                    i1, j1 = i, j 
                    return i1, j1
 
    print(find_ij(board))
    x, y = find_ij(board)
    print(x)
    print(y)


    
