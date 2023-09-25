import sys
sys.stdin = open('4837.txt','r')

def lenlen(list): # len 함수 정의
    cnt = 0
    for _ in list:
        cnt += 1
    return cnt

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

test_case = int(input())

for tc in range(test_case):
    N, K = list(map(int, input().split()))

    
    K_count = 0 # 몇개나 있는지
    for i in range(1<<12): # 전체 부분집합 구하기
        set_sum = 0
        set_list = []
        for j in range(12):
            if i & (1<<j):
                set_sum += A[j]
                set_list.append(A[j])
                print(set_list)
                print(set_sum)
    
        if set_sum == K and lenlen(set_list) == N: # 합과 길이가 N과 K와 일치하면
            K_count += 1
    if K_count >= 1:
        print(f'#{tc+1} {K_count}')
    else:
        print(f'#{tc+1} 0')
        
            


