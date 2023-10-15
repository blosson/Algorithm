# <IDEA>
# - idx (맵의 끝)와 벽이 있는 곳에 조건을 잘 주어서 idx(4, 4)에 도달하게 해야 함
#     1. 상하좌우 탐색
        
#         1) 범위 탐색 : 맵의 끝인지 확인 idx 0,0 ~ 4,4 사이 아니면 pass
        
#         2) 벽 탐색 : → idx를 하나씩 움직여서 0인지 확인
        
# - 한 번 이동할 때마다 cnt 변수를 +1씩 해주어서 cnt간의 최소값을 찾자
#     - 탐색 중에 cnt를 넘어가게 되면 과감히 함수를 종료하는 조건을 주면 좀 더 시간이 빨라질듯
# - 탐색을 다 했는데 idx(4, 4)에 도달하지 못했으면 -1을 리턴


from collections import deque

def solution(maps):
    row_len = len(maps)
    col_len = len(maps[0])
		# 델타 탐색 (4방향)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 1

    Q = deque()
    Q.append((0, 0, answer))
		maps[0][0] == 0
    while Q:
        
        x, y, answer = Q.popleft()
      
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
						# 끝에 도달하면 answer return
            if (row == row_len - 1) and (col == col_len - 1):
                return answer + 1
            if 0 <= row < row_len and 0 <= col < col_len and maps[row][col] == 1:
                Q.append((row, col, answer+1))
								# 효율성 위해 0으로 바꾸어줌
                maps[row][col] = 0

    return -1
          
    

# stack 풀이 (재귀는 너무 깊어져서 안됨)
# 이미 지나간 자리 다시 방문할 수 있또록, 다시 되돌아올 때 경로 횟수 초기화 힘듦

def solution(maps):
    answer = 9999999999999
    visited = [[0] * len(maps) for _ in range(len(maps))]
    stack = [(0, 0)]
    visited_cnt = 0
    arrived = False

    while stack:
        now = stack.pop()
        row, col = now[0], now[1]
        visited_cnt += 1
        visited[now[0]][now[1]] = visited_cnt
        print(now, visited_cnt)
        
        if row == 4 and col == 4:
            arrived = True
            if visited_cnt < answer:
                answer = visited_cnt
    
        # 조건줘서 최소값 이상은 탐색하지 않기
        if visited_cnt >= answer:
            continue
        
        if row - 1 >= 0: 
            if maps[row-1][col] == 1:
                if visited[row-1][col] == 0:
                    stack.append((row-1, col))
                    
        if row + 1 <= 4:
            if maps[row+1][col] == 1:
                if visited[row+1][col] == 0:
                    stack.append((row+1, col))
                    
        if col - 1 >= 0:
            if maps[row][col-1] == 1:
                if visited[row][col-1] == 0:
                    stack.append((row, col-1))  
                    
        if col + 1 <= 4:
            if maps[row][col+1] == 1:
                if visited[row][col+1] == 0:
                    stack.append((row, col+1))   
    
    if not arrived:
        answer = -1
        
    return answer


# 3 재귀 깊이때문에 안됨

def solution(maps):
    answer = 0
    visited = [[0] * len(maps) for _ in range(len(maps))]
    def dfs(maps, row, col):
        visited[row][col] == 1
        
        if row == 4 and col == 4:
            return answer
        
        print(row, col)
        # 상하좌우 순서로 탐색 (맵 범위조건, 벽 조건)
        if row - 1 >= 0: 
            if maps[row-1][col] == 1:
                if visited[row-1][col] == 0:
                    dfs(maps, row-1, col)
        if row + 1 <= 4:
            if maps[row+1][col] == 1:
                if visited[row+1][col] == 0:
                    dfs(maps, row+1, col)
        if col - 1 >= 0:
            if maps[row][col-1] == 1:
                if visited[row][col-1] == 0:
                    dfs(maps, row, col-1)        
        if col + 1 <= 4:
            if maps[row][col+1] == 1:
                if visited[row][col+1] == 0:
                    dfs(maps, row, col+1)
        
    dfs(maps, 0, 0)
    return answer


------
# 괜찮았던 풀이
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps): 
    global n, m
    n = len(maps)
    m = len(maps[0])
    result = bfs(0, 0, maps)
    return result

def bfs(x, y, maps):
    global n, m
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]




# dfs (시간초과)

def solution(maps):
    if len(maps) == 1 and len(maps[0]) == 1:
        return 1
    row_len = len(maps)
    vec_len = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 맵 받기
    def dfs(row, vec, count):
        if maps[row_len - 1][vec_len - 1] != 1 and count >= maps[row_len - 1][vec_len - 1]:
            return
        maps[row][vec] = count
        for x, y in zip(dy, dx):
            new_row = row + y
            new_vec = vec + x
            if new_row < 0 or new_row >= row_len or \
                new_vec < 0 or new_vec >= vec_len or \
                maps[new_row][new_vec] == 0 or \
                (maps[new_row][new_vec] != 1 and 
                 maps[new_row][new_vec] <= count + 1):
                continue
            dfs(new_row, new_vec, count + 1)

    dfs(0, 0, 1)
    goal = maps[row_len - 1][vec_len - 1]
    return goal if goal != 1 else -1