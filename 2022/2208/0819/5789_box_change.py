for tc in range(1, int(input()) + 1):

    N, Q = map(int, input().split())

    box_list = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())    # Q만큼 반복해야하므로 for문 안에 input을 넣어준다
        for j in range(R-L + 1):            # (R-L+1)만큼 반복 ex) 1-3 이면 3번 반복
            box_list[L-1+j] = i + 1         # L-1+j 값이 해당 인덱스가 됨. 여기에 i+1을 넣어준다. 
                                            # (index와 box 순서가 +1 만큼의 차이가 있으므로)
    print(f'#{tc}', *box_list)
    