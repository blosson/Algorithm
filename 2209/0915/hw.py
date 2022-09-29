# 못풀어서 같은 조였던 지원님 코드로 이해했습니다!

def post(n):
    if n:
        post(ch1[n])
        post(ch2[n])
        cal.append(tree[n])


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    for _ in range(N):
        num, *extra = input().split()
        num = int(num)
        if len(extra) == 3:
            tree[num] = extra[0]
            ch1[num] = int(extra[1])
            ch2[num] = int(extra[2])
        else:
            tree[num] = int(extra[0])

    cal = []
    post(1)

    q = []
    for i in cal:
        if i not in ['+', '-', '*', '/']:
            q.append(i)
        else:
            x = q.pop()
            y = q.pop()
            if i == '+':
                q.append(y+x)
            elif i == '-':
                q.append(y-x)
            elif i == '*':
                q.append(y*x)
            elif i == '/':
                q.append(y//x)

    print(f'#{tc} ', end='')
    print(*q)