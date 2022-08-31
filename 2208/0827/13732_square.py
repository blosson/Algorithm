'''기본적으로 가장 앞쪽 i,j 값에 있는 #을 찾고 
가장 뒷쪽 #을 찾은 뒤에 for문을 돌려 모두 #으로 채워져 있는지
검사하는 아이디어로 풀이했다.'''

def find_ij(board):                             # 가장 앞에 있는 # 인덱스 찾는 함수
    i1 = j1 = -1                                # 아래 break for문은 안 먹힌다.. 이유가 뭐지
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                i1, j1 = i, j 
                return i1, j1 

for tc in range(1, int(input()) + 1):
    
    N = int(input())
    board = [list(input()) for _ in range(N)]

    ans = 'no'                                  # 기본적으로 no로 출력
    cnt = 0                                     # 입력받은 case 안에 #이 몇 개 있는지 cnt (추후에 쓰임)
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                cnt += 1

    
    '''i1, j1 = -1, -1                          # 이거 break 끝나도 왜 계속 -1로 머물러있는지 아시나요..
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                i1, j1 = i, j   
                break
        break'''

    i1, j1  = find_ij(board)                    # 위 for문 안돼서 그냥 함수로 가장 첫 #의 인덱스 구함
                
    i2, j2 = -1, -1                             # 가장 뒤에 있는 #의 인덱스 구하기 (for문 돌면서 마지막 값이 반영되므로)
    for i in range(N):          
        for j in range(N):
            if board[i][j] == '#':
                i2, j2 = i, j

    if cnt >= 1:                                # case 안에 #이 1개 이상인 경우만 정사각형이 가능
        if cnt == 1:                            # '#'이 1개인 경우는 자기자신이 정사각형으로 yes
            ans = 'yes'
        else:
            if (i2 - i1) != (j2 - j1):          # 처음 인덱스와 끝 인덱스의 차가 다르면 정사각형이 될 수 없으므로 no
                ans = 'no'
            else:
                square_cnt = 0                  # index 처음과 끝이 모두 #으로 채워져있는지 확인할 cnt 변수
                for i in range(i1, i2 + 1):
                    for j in range(j1, j2 + 1):
                        if board[i][j] == '#':
                            square_cnt += 1
                if square_cnt == (i2 - i1 + 1) ** 2:  # 모두 채워져있으면 yes
                    ans = 'yes'

    else:                                       # 없을 경우는 no 출력
        ans = 'no'

    print(f'#{tc} {ans}')

    
