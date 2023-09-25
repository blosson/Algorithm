import sys
sys.stdin = open('1206.txt', 'r')

for tc in range(1, 11):

    N = int(input())
    buildings = list(map(int, input().split()))

    light_cnt = 0
    for i in range(2, N-2):                             # 순환
        floor_max = 0                                   # 5개 구간에서 최고층을 입력할 변수
        for j in range(i-2, i+3):
            if buildings[j] > floor_max:
                floor_max = buildings[j]
        if floor_max == buildings[i]:                   # 최고층이 3번째 (가운데라면)
            n1 = buildings[i-2]
            n2 = buildings[i-1]
            n3 = buildings[i+1]
            n4 = buildings[i+2]
            second_max = max(n1, n2, n3, n4)            # 주변 4개의 건물의 최댓값을 구한 뒤
            light_cnt += (floor_max - second_max)       # 최고층 - 2번째로 높은 건물층수를 빼서 전체 조망권 수에 더해줌

    print(f'#{tc} {light_cnt}')


    
        
    
        
