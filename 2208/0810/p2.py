from pydoc import render_doc


test_case = int(input())

for tc in range(test_case):
    arr = list(map(int, input().split()))

    n = len(arr)

    set_sum_zero = 0
    for i in range(1, 1<<n): # 공집합 제외 i값 조정
        set_sum = 0
        for j in range(n):
            if i & (1<<j):
                set_sum += arr[j]
            # j 값이 전부다 else일 때 set_sum == 0 뜨는데 어떻게 고치지
            # i 값을 조정해주면 된다! (근데 공집합이 항상 index 0이라는 보장이 있나?)
        if set_sum == 0:
            set_sum_zero += 1

    if set_sum_zero == True:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')

# 2

test_case = int(input())

for tc in range(test_case):
    arr = list(map(int, input().split()))

    n = len(arr)

    set_sum_zero = 0
    for i in range(1<<n): # 공집합 제외 i값 조정
        set_sum = 0
        for j in range(n):
            if i & (1<<j):
                set_sum += arr[j]
            # j 값이 전부다 else일 때 set_sum == 0 뜨는데 어떻게 고치지
            # 공집합은 모든 집합의 부분집합
        if set_sum == 0:
            set_sum_zero += 1

    if set_sum_zero > 1: # 공집합이 무조건 포함되어 있으므로
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')

  
    

