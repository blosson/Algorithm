
K, N, M = list(map(int, input().split()))
charging_station = list(map(int, input().split()))

for i in range(M): # 0일 때 조건식
    if i == 0:
        if charging_station[0] > K:
            print(0)
    elif i == (M - 1):
        if N - charging_station[M-1] > K:
            print(0)
    else:
        if charging_station[i] - charging_station[i-1] > K:
            print(0)



