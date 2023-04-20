# 시간초과
from collections import deque

N, M, R = map(int, input().split())
connection = [[] for _ in range(N+1)]        

for _ in range(M):                      
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)

for i in range(1, N+1):
    connection[i].sort()

order = [0] * (N+1)

def DFS(R):
    visited = [0] * (N+1)
    stack = [0] * (N+1)

    turn = 1
    top = -1

    visited[R] = 1
    order[R] = turn
    now = R
    print(turn)
    while True:
        for i in connection[now]:
            if visited[i] == 0:
                turn += 1
                top += 1
                stack[top] = now
                visited[i] = 1
                order[i] = turn
                now = i
                break
            
        else:
            if top != -1:
                now = stack[top]
                top -= 1
            else:
                break

DFS(R)
order.pop(0)
for ans in order:
    print(ans)