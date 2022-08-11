import sys
sys.stdin = open('4836.txt', 'r')


def painting(list): # 색칠하는 함수
    for i in range(10):
        for j in range(10):
            if color[0] <= i <= color[2] and color[1] <= j <= color[3]:
                color_list[i][j] += 1
    return color_list


T = int(input())
for tc in range(1, T+1):
    color_list = [[0] * 10 for _ in range(10)] # 100*100 생성
    N = int(input())
    for _ in range(N):
        color = list(map(int, input().split())) # 입력받은 값으로 
        painting(color) # 색칠하기 (+1)

    cnt = 0 # 보라색
    for i in range(10):
        for j in range(10):
            if color_list[i][j] == 2: # 두 색깔이 겹치면 (값이 2면)
                cnt += 1

    print(f'#{tc} {cnt}')

# '같은 색인 영역은 겹치지 않는다' 이 말이 같은 색은 겹칠 수 없는 게 조건인지 
# 아니면 겹치면 안돼서 내가 따로 조건을 설정해주어야 하는건지 - 이거면 따로 더 방법을 찾아보자.



    






