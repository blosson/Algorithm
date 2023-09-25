import sys
sys.stdin = open('1213.txt', 'r', encoding='UTF8')

for tc in range(1, 11):
    case_num = int(input())
    pattern = input()
    target = input()

    cnt = 0
    for i in range(len(target) - len(pattern) + 1):
        if target[i:i+len(pattern)] == pattern:
            cnt += 1

    print(f'#{tc} {cnt}')


