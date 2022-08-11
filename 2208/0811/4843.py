'''import sys
sys.stdin = open('4843.txt', 'r')'''

T = int(input())
for tc in range(T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    sorted_list = []
    for i in range(10):
        if i % 2 == 0:
            sorted_list.append(numbers[-1])
            numbers.remove(numbers[-1]) # 같은 값이 3개 있으면 전부다 사라질 수 도 있음!
        else:
            sorted_list.append(numbers[0])
            numbers.remove(numbers[0])
    print(*sorted_list) # 형식에 어떻게 출력할까 / 다른사람들은 어떻게 출력했는지

    '''print(f'#{tc}', *sorted_list)

    print(f'#{t}', end=' ')
    print(*ans)'''


  