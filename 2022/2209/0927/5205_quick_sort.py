def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot, tail  = arr[0], arr[1:]                                      # 항상 pivot을 0번 인덱스로 하는 퀵정렬

    leftside = [x for x in tail if x <= pivot]                          # 1번 ~ 마지막 인덱스까지 중에 pivot 이하는 왼쪽으로 몰고 초과는 오른쪽으로
    rightside = [x for x in tail if x > pivot]  
    
    return quick_sort(leftside) + [pivot] + quick_sort(rightside)       # 재귀를 통해 반복

for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    A = quick_sort(numbers)
    print(f'#{tc} {A[N//2]}')


