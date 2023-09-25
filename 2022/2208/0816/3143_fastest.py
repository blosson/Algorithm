def BruteForce(target, pattern):
    
    M = len(target)
    N = len(pattern)

    i = 0               # target index
    j = 0               # pattern index
    cnt = 0             # how many pattern? 

    while i < M:
        if target[i] != pattern[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

        if j == N:
            j = 0
            cnt += 1

    ans = M - ((N-1) * cnt) # 횟수의 최솟값
    return ans

T = int(input())
for tc in range(1, T+1):
    a, b = list(input().split())
    print(f'#{tc} {BruteForce(a, b)}')




        
            