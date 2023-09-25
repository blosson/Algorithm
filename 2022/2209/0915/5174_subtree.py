import sys
sys.stdin = open('5174.txt', 'r')

def preorder(node):                             # subtree 노드 개수 구하는 함수정의 : pre, in, post 다 상관없음 
    global cnt
    if node == 0:                               # 노드값이 0이면 함수종료 (노드는 1부터 시작하므로)
        return
    cnt += 1                                    # 자기 자신 노드 개수 +1
    preorder(c1[node])                          # 재귀함수 호출 (자식 노드가 없으면 0값이니 그냥 return 될 거고 아니면 앞의 과정 반복)
    preorder(c2[node])

for tc in range(1, int(input()) + 1):    
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    c1 = [0] * (E + 2)                          # (간선의 개수 + 2) 만큼 빈 리스트 생성 
    c2 = [0] * (E + 2)                          # 노드 = 간선 + 1이고 노드 번호가 1부터 시작하기에 0번 인덱스는 비워두기 때문

    for i in range(E):                          # 입력받은 arr를 순회
        p, c = arr[i*2], arr[i*2 + 1]           # 부모 - 자식 관계 순회
        if c1[p] == 0:     # left               # 비어있으면 왼쪽 자식 노드에 추가
            c1[p] = c
        else:              # right              # 다른 숫자로 차있으면 오른쪽 자식 노드에 추가
            c2[p] = c
    
    cnt = 0                                     # cnt 변수 정의
    preorder(N)                                 # 해당 노드에 대한 함수 실행

    print(f'#{tc} {cnt}')


