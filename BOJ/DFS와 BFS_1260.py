from collections import deque

# 입력 후 정점 개수 + 1만큼 배열 길이 만들기 (1번부터 시작하기 때문에 0번 인덱스는 비워둠)
N, V, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

# 연결관계 배열에 입력
for _ in range(V):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 숫자가 작은 순서대로 출력할 것이므로 정렬 (stack의 경우는 내림차순 정렬 pop()을 할 거니까)
for i in arr:
    i.sort()

# print(arr)


dfs_visited = [False] * (N + 1)


# dfs 1 재귀함수
def dfs(arr, start):
    dfs_visited[start] = True
    print(start, end=" ")

    for i in arr[start]:
        if dfs_visited[i] == False:
            dfs(arr, i)


# dfs 2 stack - stack의 경우에는 내림차순 정렬해주어야 함
# stack = []
# stack.append(M)
# while stack:
#     next = stack.pop()
#     if dfs_visited[next] == False:
#         dfs_visited[next] = True
#         print(next, end=" ")
#         for i in arr[next]:
#             if dfs_visited[i] == False:
#                 stack.append(i)


dq = deque()
bfs_visited = [False] * (N + 1)


# bfs 1 (deque) - 미리 queue에 들어가는 거 잘라주기
def bfs(arr, start):
    dq.append(start)
    bfs_visited[start] = True
    while dq:
        next = dq.popleft()
        print(next, end=" ")
        # 여기에 넣어주면 안됨! (queue 안에 두번 들어갈 수 있기 때문 )
        # bfs_visited[next] = True
        for i in arr[next]:
            if bfs_visited[i] == False:
                dq.append(i)
                # 미리 방문표시 해주기 (queue 중복 방지)
                bfs_visited[i] = True


# bfs 2 - queue에는 들어가되 while 안쪽 조건에서 걸러주기
# def bfs(v):
#     visited = [0] * (N+1)
#     queue = []
#     queue.append(v)
#     while queue:
#         now = queue.pop(0)
#         # 이런식으로 짜면 append 아래에 visited 체크 안해줘도 됨
#         if visited[now] == 0:
#             print(now, end = ' ')
#             visited[now] = 1
#             for i in adj_list[now]:
#                 if visited[i] == 0:
#                     queue.append(i)


dfs(arr, M)
print()
bfs(arr, M)
