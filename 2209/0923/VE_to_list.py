# 리스트가 아닌 다른 형태로 간선의 연결 상태 불러오는 방법
# 1
# 0번부터 V번까지, E개의 간선

# 6 8
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 3 5
# 4 5
# 5 6

V, E = map(int, input().split())
N = V + 1       # 0번부터 V번까지이므로 N = V + 1
adjlist = [[] for _ in range(N)]
for _ in range(E):
    i, j = map(int, input().split())
    adjlist[i].append(j)
    adjlist[j].append(i)

print(adjlist)
# [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]


# 2

V, E = map(int, input().split())                    # 7 8
nodes = list(map(int, input().split()))             # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

adjlist = [[] for _ in range(V + 1)]                # nodes를 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 이런식으로 입력받았을 때 리스트로 변환하는 방법

for i in range(0, len(nodes), 2):
    adjlist[nodes[i]].append(nodes[i+1])
    adjlist[nodes[i+1]].append(nodes[i])

print(adjlist)
# [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]

# 3

V, E = map(int, input().split())                    # 7 8
nodes = list(map(int, input().split()))             # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

adjlist = [[] for _ in range(V + 1)]                # nodes를 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 이런식으로 입력받았을 때 리스트로 변환하는 방법
for i in range(E):
    adjlist[nodes[2*i]].append(nodes[2*i + 1])
    adjlist[nodes[2*i + 1]].append(nodes[2*i])

