def dfs(arr, p, task):
    global max_prob
    
    if max_prob >= p:                               # prunning
        return
    if task == N:                                   # task 배분이 완료되었을 경우 max_prob 갱신
        max_prob = p
    else:
        for idx, j in enumerate(arr):
            arr.pop(idx)                            # 일을 할당한 사람 제외
            dfs(arr, p * prob[j][task], task+1)
            arr.insert(idx, j)                      # 원상복귀


tests = int(input())

for tc in range(1, tests+1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    for idx, i in enumerate(prob):
        prob[idx] = list(map(lambda x:round(x*0.01, 2), i))

    arr = [i for i in range(N)]                     # 사람
    max_prob = 0
    dfs(arr, 1, 0)
    max_prob *= 100
    print(f'#{tc} {max_prob:.6f}')                  # 소수점 7번째 자리에서 반올림 및 0 채우기