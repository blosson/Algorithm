def inorder_traversal(n):
    if n:
        inorder_traversal(ch1[n])
        print(word[n], end = '')
        inorder_traversal(ch2[n])

for tc in range(1, 11):
    N = int(input())
    E = N - 1

    # 부모를 인덱스로 자식 번호 저장
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    word = [0] * (N + 1)        # 단어를 담을 리스트

    for i in range(N):
        arr = input().split()

        if len(arr) == 4:       # 자식이 2개일 경우
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])

        if len(arr) == 3:       # 자식이 1개일 경우
            ch1[int(arr[0])] = int(arr[2])

        word[int(arr[0])] = arr[1]
    
    print(f'#{tc}', end = ' ')
    inorder_traversal(1)
    print()