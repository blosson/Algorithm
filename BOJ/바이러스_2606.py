# 1. DFS
N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# print(arr)
visited = [False] * (N + 1)
cnt = 0


def dfs(arr, start):
    visited[start] = True
    global cnt
    cnt += 1
    for i in arr[start]:
        if visited[i] == False:
            dfs(arr, i)
    return cnt - 1


print(dfs(arr, 1))

# 2. BFS
N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# print(arr)
visited = [False] * (N + 1)
cnt = 0

q = []
q.append(1)
visited[1] = True
while q:
    next = q.pop(0)
    for i in arr[next]:
        if visited[i] == False:
            q.append(i)
            visited[i] = True
            cnt += 1
print(cnt)
