N = int(input())
sg_card = set((map(int, input().split())))
M = int(input())
check_card = list(map(int, input().split()))

for i in check_card:
    ans = 0
    if i in sg_card:
        ans = 1

    print(ans, end = ' ')
    
