import sys
sys.stdin = open('4839.txt', 'r')

test_case = int(input())

for tc in range(test_case):
    P, Pa, Pb = list(map(int, input().split()))


    l = 1
    r = P

    Na = 1  # A의 경우
    while l <= r:
        c = int((l + r) / 2)
        if c == Pa:
            break
        elif c < Pa:
            l = c + 1 # 이거... 왜 + 1, -1 붙이면 안 되는지 이해 안 됨.
        else:
            r = c - 1
        Na += 1

    l = 1 # l, r 초기화
    r = P

    Nb = 1
    while l <= r:
        c = int((l + r) / 2)
        if c == Pb:
            break
        elif c < Pb:
            l = c + 1
        else:
            r = c - 1
        Nb += 1

    if Na < Nb:
        print(f'#{tc+1} A')
    elif Na > Nb:
        print(f'#{tc+1} B')
    else:
        print(f'#{tc+1} 0')