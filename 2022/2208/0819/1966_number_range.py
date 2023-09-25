def BubbleSort(numbers, N):         # BubbleSort 정의
    for i in range(N-1, 0, -1):     # 해당 i값은 아래 j의 끝값에 사용됨을 유념하자!
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

for tc in range(1, int(input()) + 1):

    N = int(input())
    numbers = list(map(int, input().split()))

    print(f'#{tc}', *BubbleSort(numbers, N))



    


