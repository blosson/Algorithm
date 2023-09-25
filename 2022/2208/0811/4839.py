import sys
sys.stdin = open('4839.txt', 'r')

test_case = int(input())

for tc in range(test_case):
    P, Pa, Pb = list(map(int, input().split()))

    book = list(range(1, P+1))
    l = 1
    r = P

    Na = 1
    while l <= r:
        c = int((l + r) / 2)
        if book[c] == Pa:
            break
        elif book[c] < Pa:
            l = c + 1
        else:
            r = c - 1
        Na += 1

    l = 1
    r = P

    Nb = 1
    while l <= r:
        c = int((l + r) / 2)
        if book[c] == Pb:
            break
        elif book[c] < Pb:
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
