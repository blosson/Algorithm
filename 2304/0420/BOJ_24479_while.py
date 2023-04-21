N, M, R = map(int, input().split())
connection = [[] for _ in range(N+1)]

for _ in range(M):                      
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)

for i in range(1, N+1):
    connection[i].sort(reverse=True)        # 후입선출 구조의 stack이므로 반대로 내림차순으로 정렬 
                                            # 연결관계가 [4, 3, 2, 1] 이런식으로 정렬되어 있어야 for문을 돌리면서 
                                            # pop했을 때 1, 2, 3, 4 순으로 나와 오름차순으로 탐색할 수 있음
                                            

order = [0] * (N+1)

def DFS(R):
    visited = [0] * (N+1)                   # 방문여부 체크 리스트
    stack = [R]                             # 시작지점을 stack에 넣음

    turn = 0
    while stack:                            # 방문할 정점이 존재하는 동안
   
        now = stack.pop()                   # 방문했으므로 stack에서 pop
        if visited[now] == 0:               # 방문하지 않았으면 (stack에 같은 정점이 중복으로 들어갈 수 있으므로)
            turn += 1                       
            order[now] = turn               # now 정점의 순서에 넣어줌
            visited[now] = 1                # 방문여부 체크
            for i in connection[now]:       # 현재 정점에서 연결된 정점들을 순회
                if visited[i] == 0:         # 방문하지 않았으면 방문할 리스트(stack)에 추가
                    stack.append(i)
               
DFS(R)
order.pop(0)                                # 정점은 1부터 시작하므로 pop(0)
for ans in order:
    print(ans)