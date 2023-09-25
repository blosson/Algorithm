def route(i, j, value_sum):                         
    global ans                                  # 단순조회면 global을 안 넣어도 되나 수정할 시에는 반드시 global!

    if i == N or j == N:                        # 범위 밖을 벗어나면 return 
        return

    if i == j == N-1 and value_sum < ans:       # 도착했을 때(가장오른쪽 아래) 다 더한 값이 현재까지의 최솟값보다 작으면 대체
        ans = value_sum
        return

    elif value_sum >= ans:                      # 현재까지의 합이 최솟값보다 크면 뒤는 볼 필요 없이 return (시간절약)
        return

    for di, dj in delta:                        # delta를 순회하면 총 2번함 1번째 - i+1,j+0 / 2번째 - i+0,j+1              
        mi, mj = i + di, j + dj                 
        if 0 <= mi < N and 0 <= mj < N:         # 델타롤 이동한 인덱스가 범위 안에 존재하면 계속
            route(mi, mj, value_sum + numbers[mi][mj])  # 이때 value_sum에 다음 이동할 곳의 값을 더해줌(numbers[mi][mj])

delta = [(1, 0), (0, 1)]                        # delta
for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')                          # 무한히 큰 양수
    route(0, 0, numbers[0][0])                  # i, j, 시작지점 값
    
    print(f'#{tc} {ans}')


