import sys
sys.stdin = open('1213.txt', 'r', encoding='UTF8')

for tc in range(1, 11):

    case_num = int(input())
    pattern = input()
    target = input()

    i = 0 # target의 index
    j = 0 # pattern의 index

    M = len(target) # target의 길이
    N = len(pattern) # pattern의 길이
    
    cnt = 0
    while i <= M-1:
        if target[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == N:
            cnt += 1
            j = 0
    
    print(f'#{tc} {cnt}')




