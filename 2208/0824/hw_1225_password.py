import sys
sys.stdin = open('1225.txt','r')

# 문제 설명도 이상하고 testcase에 관련된 명시도 안 되어있어서 엄청 헤맸다..

for tc in range(1, 11):                             
    int(input())
    num_list = list(map(int, input().split()))

    while True:
        for i in range(1, 6):                               # 한 사이클 반복 1~5
            if num_list[0] - i <= 0:                        # 제일 앞 index의 값 - i가 <= 0면
                num_list.pop(0)                             # pop하고 0을 append
                num_list.append(0)
                break     
            else:
                num_list.append(num_list.pop(0) - i)

        if num_list[-1] == 0:                               # break - break 연속으로 하니까 while문 안빠져나가졌는데 이렇게하니까 빠져나가진다! (굿)
            break

    print(f'#{tc}', *num_list)