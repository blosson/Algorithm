for tc in range(1, int(input()) + 1):

    number = input()
    counts = [0] * 12               # 인덱스 스무스하게 넣기 위해 뒤에 두 칸을 더 추가해줌 (3개씩 검사하기 때문)

    for i in number:
        counts[int(i)] += 1         # str -> int로 바꾸면서 counts 리스트에 개수별로 넣어줌


    '''while number > 0:            # 이렇게 하면 000000 또는 005406 이런 것들을 받을 수 없다.
        counts[number % 10] += 1    # 해결방법을 나중에 한 번 찾아보자.
        number //= 10
        if number == 0:
            counts[0] += 1
            break'''

    run = 0
    tri = 0
    i = 0
    while i <= 10:                  # for문을 쓰면 333333 같은 것들을 지나칠 수 있으므로 while-continue로 해주는 게 좋음
        if counts[i] >= 3:
            counts[i] -= 3
            tri += 1
            continue

        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue
        i += 1

    if (tri == 2) or (run == 2) or (tri == 1 and run == 1): # 이렇게 안하고 tri, run을 모두 babygin 변수로 줘서
        print(f'#{tc} 1')                                   # babygin == 2: 이런식으로 해줘도 될듯
    else:
        print(f'#{tc} 0')
        
        
    
    
