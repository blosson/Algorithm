# 재귀로 dfs 구현
def dfs(v):
    print(v)
    visited[v] = 1
    for w in adjlist[v]:
        if visited[w] == 0:
            dfs(w)


# 인접한 번호들을 알려주는 리스트
adjlist = [[1, 2],      # index 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]          # 6
           ]

N = int(input())
visited = [0] * N

dfs(0)