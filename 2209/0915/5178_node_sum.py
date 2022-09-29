import sys
sys.stdin = open('5178.txt', 'r')

def node_sum(node):                                             # 해당 노드의 값 구하는 함수 (노드 값은 자식들의 합)
    if (node * 2) <= N and (node * 2 + 1) <= N:                 # 자식이 2개일 경우
        return node_sum(node * 2) + node_sum(node * 2 + 1)      # 재귀 호출해서 반복
    elif (node * 2) <= N and (node * 2 + 1) > N:                # 자식이 1개일 경우 (완전 이진트리이므로 자식이 하나라면 무조건 왼쪽 자식임)
        return node_sum(node * 2)
    else:                                                       # 자식이 없을경우 : 리프 노드이므로 해당 값 출력
        return node_list[node]              

for tc in range(1, int(input()) + 1):        
        
    N, M, L =  map(int, input().split())
    node_list = [0] * (N + 1)                                   # 각 노드의 합을 담을 리스트 (index는 노드 번호)
    for i in range(M):                                          # 리프의 개수만큼 반복
        leaf_index, leaf_value = map(int, input().split())     
        node_list[leaf_index] = leaf_value                      # 리스트에 리프값 넣어주기

    print(f'#{tc} {node_sum(L)}')
