V, E = map(int, input().split())                    # 7 8
nodes = list(map(int, input().split()))             # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

adjlist = [[] for _ in range(V + 1)]                # nodes를 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 이런식으로 입력받았을 때 리스트로 변환하는 방법
for i in range(E):
    adjlist[nodes[2*i]].append(nodes[2*i + 1])
    adjlist[nodes[2*i + 1]].append(nodes[2*i])

visited = [0] * (V+1)                               # V+1만큼 인덱스 생성. 사실 V개만 생성해도 되나 시작지점이 1부터므로 인덱스 맞춰주기 쉽게 하기 위해
stack = [0] * (V+1)

def dfs(v):                                         # v = 시작지점
    
    top = -1                                        # stack 쌓기 위해 기본 -1 설정
    print(v, end = ' ')                             # 시작 지점 출력
    visited[v] = 1                                  # 시작 지점 방문 표시
    
    while True:
        for w in adjlist[v]:                    
            if visited[w] == 0:                     # w(다음 지점)를 아직 방문하지 않았으면
                top += 1                            # top을 1 올려주고 그 자리에 v값을 저장
                stack[top] = v

                v = w                               # 다음 이동할 지점을 v로 바꿔줌
                print(v, end = ' ')
                visited[v] = 1                      # 방문 지점을 출력해주고 방문 표시 
                break                               # 해당 v에 대해서 다시 탐색해야하므로 for문 종료하고 다시 while문으로 ㄱㄱ
        
        else:                                       # 다음 방문 지점이 없거나 이미 다 방문했으면 (for-else문)
            if top != -1:                           # stack이 비어있지 않으면 다시 뒤로 돌아가고 (v값에 stack[top] 할당함으로써 해당 v로 다시 while문을 돌려줌 )
                v = stack[top]
                top -= 1
            else:                                   # top이 -1이면 더이상 방문할 곳이 없고 처음으로 돌아왔다는 의미이므로 while문 종료
                break


dfs(1)                                              # 1 2 4 6 5 7 3 
    


    