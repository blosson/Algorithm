# 112 ms

# 게으른 손민혁은 반성합니다..

computer_num = int(input())             # 컴퓨터 갯수
N = int(input())                        # 연결된 쌍의 갯수 (노드 갯수)

visited = [0] * (computer_num+1)        # visited list 생성 (1번 컴퓨터부터 시작하므로 +1 해주어야함)
linked = [[] * (computer_num+1) for _ in range(computer_num+1)]     # 연결관계 표시하기 위한 2차원 리스트


for _ in range(N):                      # 연결된 노드 갯수만큼 반복
    x, y = map(int, input().split())    # 연결관계 입력 받기
    linked[x].append(y)                 # 연결관계 2차원 리스트에 추가
    linked[y].append(x)

cnt = 0                                 # 1번 컴퓨터로부터 연결된 컴퓨터의 갯수

def DFS(virus):                         # DFS 함수 구현 (아 이거 아직도 재귀 헷갈림...)
    global cnt                          # 글로벌 변수 설정

    visited[virus] = 1                  # 방문 표시

    for i in linked[virus]:             # 2차원 리스트에 virus를 파라미터로 받은 곳 순회
        if (visited[i] == 0):           # 아직 방문 안했으면 DFS 돌린다.
            DFS(i)
            cnt += 1                    # 다 돌렸으면 cnt + 1

DFS(1)                                  # 1번 컴퓨터부터 시작하므로 DFS(1)
print(cnt)                              # 정답 출력


