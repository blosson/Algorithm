import sys
sys.stdin = open('2001.txt', 'r')

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]  # N*N input 리스트 만들어주기

    box_sum_max = 0
    for i in range(N-M+1):                      # 행, 열 각각 N-M+1 만큼 반복하며 사각형의 합을 구할 수 있다!
        for j in range(N-M+1):
            box_sum = 0                         # M*M 박스의 합을 넣어줄 변수
            for k in range(i, i+M):             # i~(i+M-1)행까지 순회하며 더하기 위한 for문
                row_sum = 0                     # M*M 박스의 각 행의 합을 넣어줄 변수 
                for l in range(j, j+M):         # i~(i+M-1)열까지 순회하며 더하기 위한 for문
                    row_sum += board[k][l]      # M*M 박스의 한 행의 합
                box_sum += row_sum              # 각 행의 합을 박스의 합에 넣어준다.
            if box_sum > box_sum_max:           # 현재 박스의 합이 기존 박스의 합의 MAX보다 크면
                box_sum_max = box_sum           # 새로운 MAX가 탄생

    print(f'#{tc} {box_sum_max}')


                
   
    