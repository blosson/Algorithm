def cost_min(product):
    global ans, factory_sum
    
    if product >= N:                            # 마지막 제품까지 돌았으면 현재까지의 최솟값과 현재 비용합을 비교
        if ans > factory_sum:
            ans = factory_sum
        return
    
    if ans <= factory_sum:                      # 현재 비용합이 이미 최솟값을 넘었으면 뒤도 안 돌아보고 버려버림
        return 

    for i in range(N):
        if visited[i] == 0:                     # 이미 생산 결정된 공장이 아니라면 
            visited[i] = 1                      # visited 체크 해주고 해당 비용을 factory_sum에 더해줌
            factory_sum += cost[product][i]
            cost_min(product + 1)               # 재귀 호출
            visited[i] = 0                      # 값을 다시 계산해야하니 다시 visited 초기화
            factory_sum -= cost[product][i]     # factory_sum도 전 단계로 빼줌


for tc in range(1, int(input()) + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    ans = float('inf')                          # 정답 변수 (무한값으로 초기 설정)
    visited = [0] * N                           # 방문 확인 (공장)
    factory_sum = 0                             # 케이스별 비용 합

    cost_min(0)                                 # 0번 제품부터 시작
    print(f'#{tc} {ans}')


        
        
