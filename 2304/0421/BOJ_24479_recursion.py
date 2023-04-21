import sys
input = sys.stdin.readline              # input을 여러 줄로 받을 때 시간단축 가능
sys.setrecursionlimit(10**7)            # 재귀 깊이 증가

N, M, R = map(int, input().split())
connection = [[] for _ in range(N+1)]        

for _ in range(M):                      
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)

for i in range(1, N+1):                 # 작은 숫자인 정점부터 순회하니 오름차순 정렬
    connection[i].sort()

order = [0] * (N+1)                     # 방문 순서 리스트 (0번 정점이 없으니 N+1)
visited = [0] * (N+1)                   # 방문 여부 표시 리스트 (0 or 1)
turn = 0                                # 순서 변수 (함수 시작 시에 +1 해줄 거니 초기값은 0)
visited[R] = 1                          # 시작점 표시

def DFS(R):
    global turn                         

    turn += 1                           
    order[R] = turn                     # 정점 번호에 순서 표시

    for i in connection[R]:             # 해당 정점에 연결된 다른 정점들을 순회해서
        if visited[i] == 0:             # 방문하지 않았으면 방문표시하고 재귀 출력
            visited[i] = 1
            DFS(i)

DFS(R)
order.pop(0)                            # 0번 정점은 존재하지 않으므로 pop으로 제거
for ans in order:
    print(ans)

