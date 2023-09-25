for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    tree = [0]                          # 노드 번호별 값이 들어갈 리스트

    for i in numbers:                   # 입력받은 값들을 차례로 꺼내서 tree 리스트에 담아줌
        tree.append(i)                   
        n = len(tree) - 1               # 현재 노드번호 = 리스트길이 - 1
        while n//2 > 0:                 # 부모 노드가 존재하면
            if tree[n] < tree[n//2]:    # 부모 노드값이 자식 노드값보다 크면 자리 바꿔줌
                tree[n], tree[n//2] = tree[n//2], tree[n]
                n //= 2                 # 부모가 더 있는지 확인하기 위해 2로 나눈 몫으로 대체
            else:
                break

    ans = 0                             # 조상값을 더해줄 변수

    while N//2 > 0:                     # 조상이 존재하는 동안 반복
        N //= 2
        ans += tree[N]                  # 조상값 더해주기

    print(f'#{tc} {ans}')

