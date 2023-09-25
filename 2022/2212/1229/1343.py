board = input()

board_len = len(board)
polyomino = []
cnt = 0
for i in range(board_len):      
    if board[i] == 'X':                             # X일 때
        cnt += 1

        if cnt == 4:                                # cnt 4면 AAAA 추가해주고 cnt 초기화
            polyomino.append('AAAA')
            cnt = 0

        elif cnt == 1 and i == board_len - 1:       # i가 마지막 번호이고 cnt가 1이면 불가능이므로 -1
            polyomino = -1
 
        elif cnt == 2 and i == board_len - 1:       # i가 마지막 번호이고 cnt 2면 BB추가
            polyomino.append('BB')

        elif cnt == 3 and i == board_len - 1:       # i가 마지막 번호이고 cnt 2면 BB추가
            polyomino = -1


    else:                                           # .일 경우

        if cnt % 2 == 1:                            # cnt가 홀수일 때는 때려죽여도 폴리오미노 불가능이므로 -1
            polyomino = -1
            break
        
        elif cnt == 2:                              # cnt가 2면 BB. 추가
            polyomino.append('BB.')
            cnt = 0

        elif cnt == 0:                              # 0이면 .추가
            polyomino.append('.')


if polyomino == -1:                 # 불가능한 경우
    print(polyomino)
else:                               # 가능한 경우 출력
    print(*polyomino, sep='')