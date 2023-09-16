import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# n이 세로, m이 가로
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# print(maps)

# 빈칸인 인덱스를 zero_list에 담아줌
zero_list = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            zero_list.append((i, j))
# print(zero_list)

# 새로 벽을 세울 3개의 빈 칸을 조합으로 뽑음
selected_zeros = list(combinations(zero_list, 3))
# print(selected_zeros)

# 벽을 세우고 순회 시작
max_cnt = 0
for zeros in selected_zeros:
    # 벽 3개 세우기 (2차원 배열이기 때문에 deepcopy())
    new_maps = copy.deepcopy(maps)
    for zero in zeros:
        row, col = zero[0], zero[1]
        new_maps[row][col] = 1
    # print(maps, new_maps)
    
    for i in range(n):
        for j in range(m):
            # 바이러스가 있는 곳만 탐색 (bfs)
            if new_maps[i][j] == 2:
                dq = deque()
                dq.append((i, j))
                # 방문표시를 3으로 해주려했는데 어차피 이미 갔던 곳은 다시 방문 안하니 pass
                # new_maps[i][j] = 3
                while dq:
                    next = dq.popleft()
                    x, y = next[0], next[1]
                    # print(x, y)
                    # 델타 4 방향 탐색
                    for _ in range(4):
                        new_i = x + dx[_]
                        new_j = y + dy[_]

                        # 조건 범위 안에 있고 빈 공간이면 (0이면) dq에 넣고 방문처리 (3)
                        if 0 <= new_i < n and 0 <= new_j < m and new_maps[new_i][new_j] == 0:
                            dq.append((new_i, new_j))
                            new_maps[new_i][new_j] = 3

    # print(new_maps)
    # 안전지대 개수 세기
    cnt = 0
    for i in range(n):
        for j in range(m):
           if new_maps[i][j] == 0:
                cnt += 1
    
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)

                

    


    


