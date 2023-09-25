for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0                        # 정답 변수
    for i in range(N):              # 행
        cnt = 0
        for j in range(M):
            if arr[i][j]:           # 1이 있으면 cnt +=1 이렇게 해주면 굳이 슬라이싱 하지 않아도 효율적으로 찾기 가능
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0


    for j in range(M):              # 열
        cnt = 0                     # 어차피 가로 cnt의 max는 maxV에 저장되어 있으므로 cnt 변수 또 써도 사용해도 상관 없음
        for i in range(N):          # 열의 경우에도 이렇게 가능
            if arr[i][j]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxV}')



        

    