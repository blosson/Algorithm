def inorder(n):                             # 중위순회로 번호 넣어주는 함수
    if n:
        if (n*2) <= N:                      # 왼쪽 자식 있으면 재귀 함수 호출
            inorder(n*2)
        order_list.append(n)                # 자기자신의 값 리스트에 추가
        if (n*2 + 1) <= N:                  # 오른쪽 자식 있으면 재귀 함수 호출
            inorder(n*2 + 1)

for tc in range(1, int(input()) + 1):

    N = int(input())

    order_list = []                         # 중위번호 순회 순서대로 담을 리스트
    node_list = [0] * (N + 1)               # 해당 노드 번호의 값을 담을 리스트

    inorder(1)                              # 중위순회로 order_list 채우기

    k = 1
    for i in order_list:                    # order_list 순서대로 node_list index로 끌어와서 k값을 넣어줌
        node_list[i] = k                        
        k += 1                              # k값 1씩 더해줘서 1, 2, 3, 4 ... 이렇게 값이 입력될 수 있게하기 위해!

    print(f'#{tc} {node_list[1]} {node_list[N//2]}')


    