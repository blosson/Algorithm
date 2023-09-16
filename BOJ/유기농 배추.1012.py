# bfs 풀이 (dq에 append 직후 방문처리 - 큐이기 때문에 가능)
import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
# 델타 조건 조건 만들어주기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(tc):
    # 배추밭 생성
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1
    # print(farm)

    # 방문 표시할 이차원 리스트, 미생물 개수(cnt) 변수 초기화
    visited = [[False] * (m) for _ in range(n)]
    cnt = 0
    # x : 세로, y : 가로 / m : 가로, n : 세로
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                if visited[i][j] == False:
                    # bfs 시작
                    cnt += 1
                    # print(cnt, (i, j))
                    dq = deque()
                    dq.append((i, j))
                    # print(stack)
                    while dq:
                        next = dq.popleft()
                        x, y = next[0], next[1]
                        # print(x, y)
                    
                        for _ in range(4):
                            # 맵 조건, 방향 탐색
                            new_x = x + dx[_]
                            new_y = y + dy[_]
                            # 다음 이동할 곳이 맵 범위 안에 있고 아직 방문하지 않았으면
                            if 0 <= new_x < n and 0 <= new_y < m:
                                if farm[new_x][new_y] == 1 and visited[new_x][new_y] == False:
                                    dq.append((new_x, new_y))
                                    # print((i, j), stack, cnt)
                                    visited[new_x][new_y] = True
    
    print(cnt)



# bfs 풀이 (while 들어와서 visited 처리)
import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(tc):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1
    # print(farm)

    visited = [[False] * (m) for _ in range(n)]
    cnt = 0
    # x : 세로, y : 가로 / m : 가로, n : 세로
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                if visited[i][j] == False:
                    # bfs 시작
                    cnt += 1
                    # print(cnt, (i, j))
                    dq = deque()
                    dq.append((i, j))
                    # print(stack)
                    while dq:
                        next = dq.popleft()
                        x, y = next[0], next[1]
                        # print(x, y)

                        if visited[x][y] == False:
                            visited[x][y] = True
                            # print(visited)
                    
                            for _ in range(4):
                                # 맵 조건, 방향 탐색
                                new_x = x + dx[_]
                                new_y = y + dy[_]
                                if 0 <= new_x < n and 0 <= new_y < m:
                                    if farm[new_x][new_y] == 1 and visited[new_x][new_y] == False:
                                        dq.append((new_x, new_y))
                                        # print((i, j), stack, cnt)
    
    print(cnt)


# # dfs 풀이 (stack)
import sys
input = sys.stdin.readline

tc = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(tc):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1
    # print(farm)

    visited = [[False] * (m) for _ in range(n)]
    cnt = 0
    # x : 세로, y : 가로 / m : 가로, n : 세로
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                if visited[i][j] == False:
                    # dfs 시작
                    cnt += 1
                    # print(cnt, (i, j))
                    stack = [(i, j)]
                    # print(stack)
                    while stack:
                        next = stack.pop()
                        x, y = next[0], next[1]
                        # print(x, y)

                        if visited[x][y] == False:
                            visited[x][y] = True
                            # print(visited)
                    
                            for _ in range(4):
                                # 맵 조건, 방향 탐색
                                new_x = x + dx[_]
                                new_y = y + dy[_]
                                if 0 <= new_x < n and 0 <= new_y < m:
                                    if farm[new_x][new_y] == 1 and visited[new_x][new_y] == False:
                                        stack.append((new_x, new_y))
                                        # print((i, j), stack, cnt)
    
    print(cnt)