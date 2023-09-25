V, E = map(int, input().split())                    # 7 8
nodes = list(map(int, input().split()))             # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

adjlist = [[] for _ in range(V + 1)]                # nodes를 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 이런식으로 입력받았을 때 리스트로 변환하는 방법

for i in range(0, len(nodes), 2):                   # range 차를 2씩 둬서 리스트에 저장
    adjlist[nodes[i]].append(nodes[i+1])
    adjlist[nodes[i+1]].append(nodes[i])

visited = [0] * (V+1)                               # 방문 표시
def dfs(v):

    print(v)
    visited[v] = 1

    for w in adjlist[v]:
        if visited[w] == 0:
            dfs(w)                                  # 이러면 재귀함수 호출하면서 반복하며 전부 다 돌게 됨

dfs(1)                                              # 1 2 4 6 5 7 3
    