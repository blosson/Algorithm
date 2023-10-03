# BOJ_11724 :: 연결요소의 개수 (S2)

def dfs(start):                         # DFS 정의
    visited[start] = True

    for i in adj_list[start]:
        if visited[i] == False:
            dfs(i)
    
N, M = map(int, input().split())        

adj_list = [[] for _ in range(N+1)]     # 연결리스트 생성
for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

visited = [False] * (N + 1)

cnt = 0                                 # 연결요쇼의 개수 (정답변수)
for i in range(1, N+1):                 # 1부터 각각의 정점을 순회해서 방문한 적이 없으면 + 1
    if visited[i] == False:             # (연결되어 있으면 True이기 때문에 cnt는 그대로)
        cnt += 1
        dfs(i)

print(cnt)

    