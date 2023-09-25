# 1. 재귀
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

# print(arr)
visited = [0] * (N + 1)
visiting_order = 0

def dfs(R):
    global visiting_order
    visiting_order += 1
    visited[R] = visiting_order
    for i in arr[R]:
        if visited[i] == 0:
            dfs(i)

dfs(R)
for i in visited[1::]:
    print(i)


# 2. stack
N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort(reverse=True)

# print(arr)
visited = [0] * (N + 1)
visiting_order = 0
stack = [R]
while stack:
    next = stack.pop()
    if visited[next] == 0:
        visiting_order += 1
        visited[next] = visiting_order
        for i in arr[next]:
            if visited[i] == 0:
                if not i in stack:
                    stack.append(i)

visited.pop(0)
for i in visited:
    print(i)
    
    
