for tc in range(1, int(input()) + 1):

    N = int(input())

    ans = []
    for i in range(N):
        pascal = []
        for j in range(i+1):
            if j == 0 or j == i:
                pascal.append(1)
            else:
                pascal.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(pascal)

    print(f'#{tc}')
    for _ in ans:
        print(*_)





