def binary_serach(n, arr, key):         # n은 arr의 길이, arr는 정렬된 리스트, key는 목표값
    global cnt

    left = 0                            # 왼쪽 index
    right = n - 1                       # 오른쪽 index
    just_before = 0                     # 직전에 왼쪽 방문했으면 left == 1, 오른쪽이면 right == 2 / 처음이면 0
    
    while left <= right:
        mid = ((right + left) // 2)     # 초기 중앙값 (문제에서 제시해준 조건)
        
        if arr[mid] == key:             # 목표값과 일치하면 cnt = 1로 변경 (기존 cnt값은 0)
            cnt = 1
            return

        elif arr[mid] > key:            # 목표값이 mid보다 작은 경우 (오른쪽 범위를 싹둑해야함 = 왼쪽으로 가야함)
            if just_before == 1:        # 그런데 직전에 왼쪽을 방문했으면 매몰차게 버림
                return                   
            else:                       # 처음 방문하거나 직전에 오른쪽을 방문했으면
                right = mid - 1         # 오른쪽 범위를 줄여주고
                just_before = 1         # 왼쪽 방문 표시

        else:                           # 목표값이 mid보다 큰 경우 (왼쪽 범위를 싹둑해야함 = 오른쪽으로 가야함)
            if just_before == 2:        # 위값과 동일
                return
            else:
                left = mid + 1
                just_before = 2

    return                              # 목표값이 없을 때

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A_numbers = list(map(int, input().split()))
    B_numbers = list(map(int, input().split()))
    A_numbers = sorted(A_numbers)       # 정렬
    AB_numbers = []                     # A에도 존재하는 B값들을 넣어줄 리스트

    for i in B_numbers:                 # A에 존재하는 B값들을 넣어주는 과정
        if i in A_numbers:
            AB_numbers.append(i)


    ans = 0                             # 정답 변수
    for i in AB_numbers:
        cnt = 0                         # cnt = 0으로 초기화 (계속 순회돌거니까)
        binary_serach(N, A_numbers, i)  
        if cnt == 1:                    # cnt가 1이면 (첫 미드값이 key값, 두 번만에 찾기(왼쪽 또는 오른쪽), 번갈아가며 찾는 경우)
            ans += 1

    print(f'#{tc} {ans}')               



