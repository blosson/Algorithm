# DFS 풀이 (재귀)
import sys
sys.setrecursionlimit((10**7))
input = sys.stdin.readline

# 델타 탐색 (대각선 포함 8방향)
d_row = [-1, -1, -1, 0, 1, 1, 1, 0]
d_col = [-1, 0, 1, 1, 1, 0, -1, -1]

# DFS (재귀)
def dfs(x, y):
    # 방문했으니 0으로 처리
    maps[x][y] = 0 
    for _ in range(8):
        row = x + d_row[_]
        col = y + d_col[_]
        
        if 0 <= row < h and 0 <= col < w and maps[row][col] == 1:
            dfs(row, col)
    return
    
while True:
    w, h = map(int, input().split())
    # 0 0이 나오면 마지막 입력값이므로 while 종료
    if w == 0 and h == 0:
        break

    # input값으로 지도 생성
    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))
    # print(maps)

    # maps 순회하면서 1인 경우에 dfs함수 통해서 섬의 개수 탐색
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                # 섬의 개수 +1
                cnt += 1
                dfs(i, j)
    
    print(cnt)
                    


# BFS 풀이
import sys
from collections import deque
sys.setrecursionlimit((10**7))
input = sys.stdin.readline

# 델타 탐색 (대각선 포함 8방향)
d_row = [-1, -1, -1, 0, 1, 1, 1, 0]
d_col = [-1, 0, 1, 1, 1, 0, -1, -1]

# BFS 함수
def bfs(x, y):
    # 방문했으니 0으로 처리
    dq = deque()
    dq.append((x, y))
    while dq:
        next = dq.popleft()
        a, b = next[0], next[1]
        if maps[a][b] == 1:
            maps[a][b] = 0
            for _ in range(8):
                row = a + d_row[_]
                col = b + d_col[_]

                if 0 <= row < h and 0 <= col < w and maps[row][col] == 1:
                    dq.append((row, col))
                   
    return
    
while True:
    w, h = map(int, input().split())
    # 0 0이 나오면 마지막 입력값이므로 while 종료
    if w == 0 and h == 0:
        break

    # input값으로 지도 생성
    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))
    # print(maps)

    # maps 순회하면서 1인 경우에 dfs함수 통해서 섬의 개수 탐색
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                # 섬의 개수 +1
                cnt += 1
                # print((i, j), cnt)
                bfs(i, j)
    
    print(cnt)    
    

            
    
