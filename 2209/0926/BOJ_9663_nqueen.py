'''
기본적으로 완전탐색을 한다고 가정했을 때 시간은 많이 소모되겠지만 구현하기 어려운 것
1. 어떻게 N_Queen 조건을 주어 cnt를 할 것인가? 
    1) 행, 열, 대각선 등 visited 리스트르 만들어서? (대각선은 어떻게 구현할지 감도 안 잡힘)
    

2. 방법은 어떻게 구현할 것인가?
    2차원 배열? N * N 리스트 만들어서 퀸이 위치한 곳을 1로 표시?
    1) 반복? : N이 14일 때 for문을 14번 돌려야하나.. 분명 이 방향은 아닐 거고 분명 prunning 할 수 있는 조건이 있을 거다. Dammmm
    2) 재귀? : 깊이 문제가 있긴 하겠지만 이것도 분명 함수 어딘가에서 prunning을 해주어야 할 것 같다.

Don't know what to do~~~~~~~
    
'''

def prunning(x):                    # 백트래킹 (조건에 안 맞는 것들은 과감하게 버려버리는 살벌함 ㄷㄷㄷ)
    for i in range(x):              # x번째 행 직전지 순회하며 검사
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):  # 열이 겹치지 않고(인덱스의 값, 그리고 행은 이미 인덱스로 분리되어있으므로 괜찮) - 가로, 세로
            return False                                            # 인덱스간의 차가 인덱스 간의 차와 같지 않으면 - 대각선 검사
    return True                                                     # 백트래킹에서 살아남는 친구들임

def playing(x):
    global cnt

    if x == N:                      # N-1번째 행까지 다 체크하고 왔으면 (= N-Queen 배치가 가능하면)
        cnt += 1                    # cnt +1 해줌
        return
    
    else:                           # 0 ~ N-1번째 행이라면 
        for i in range(N):          # 열 인덱스 순회
            row[x] = i              # 해당 행에 대한 열 index 값을 넣어주고 (0, 1, 2, 3 ... N-1)
            if prunning(x):         # N_Queen을 배치할 수 있는 행이라면
                playing(x+1)        # 다음 행으로 넘어감 (재귀호출)
    
   
N = int(input())
row = [0] * N                       # 1차원 배열 생성(2차원이 아닌 이유는 행(index)에 열value(index)를 넣어주면 되기 때문!)
cnt = 0                             # N-Queen 개수 (정답변수)

playing(0)                          # index 0번 행부터 시작
print(cnt)

 