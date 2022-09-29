# 인접한 번호들을 알려주는 리스트
adjlist = [[1, 2],      # index 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]          # 6
           ]

N = 7                   # 정점의 개수
visited = [0] * N       # visited 생성
stack = [0] * N         # stack 생성

def dfs(v, N):          # v는 시작지점, N은 정점의 개수

    top = -1
    print(v)            # 방문
    visited[v] = 1      # 시작점 방문 표시

    while True:
        for w in adjlist[v]:
            if visited[w] == 0:     # v의 인접 정점 중 방문 안 한 정점 w가 있으면
                top += 1
                stack[top] = v      # v를 stack에 push
                v = w               # v <- w (w에 방문)
                print(v)
                visited[w] = 1      # 방문 표시
                break
        
        else:                       # w가 없으면 (for-else문)
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while문 종료

dfs(0, N)







