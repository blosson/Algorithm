
# 동준님 아이디어 : 각각의 리스트를 만들어서 for문으로 출력해준다!

for tc in range(1, int(input()) + 1):
    print(f'#{tc}')

    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    spin90 = []
    for j in range(N):
        plus_list = []
        for i in range(N-1, -1, -1):
            plus_list.append(numbers[i][j])
        spin90.append(plus_list)


    spin180 = []
    for i in range(N-1, -1, -1):
        plus_list = []
        for j in range(N-1, -1, -1):
            plus_list.append(numbers[i][j])
        spin180.append(plus_list)


    spin270 = []
    for j in range(N-1, -1, -1):
        plus_list = []
        for i in range(N):
            plus_list.append(numbers[i][j])
        spin270.append(plus_list)

    for i in range(N):
        print(*spin90[i], sep ='', end = ' ')
        print(*spin180[i], sep = '', end = ' ')
        print(*spin270[i], sep = '')
    

'''for _ in range(N):
    for i in range(N):
        print(numbers[N-1-i][N-N], end = '')
    for i in range(N):
        print(numbers[N-1-0][N-1-i], end = '')
    for i in range(N):
        print(numbers[i][N-1], end = '')'''


# 자기끼리는 붙여쓰고 남들하고는 띄어쓰기 하려면?
# 한번 90도 돌리고 계속 돌리는 식으로 해서 출력하면 어떨까?
# 아니면 애초에 똑같은 행렬에서 내가 힘의로 추출하는 건(왼쪽, 아래쪽, 오른쪽 이렇게!) - 이게 제일 가능성 있는듯

        