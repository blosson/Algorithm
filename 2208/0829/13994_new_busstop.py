for tc in range(1, int(input()) + 1):
    N = int(input())
    bus_stop = [0] * 1001                       # 기본적으로 정류장 count 리스트를 만들어서 채우는 아이디어!

    for _ in range(N):
        bus, A, B = map(int, input().split())
        bus_stop[A] += 1                        # 처음과 끝 정류장은 항상 정차하므로 +1
        bus_stop[B] += 1

        if bus == 1:
            for i in range(A+1, B):             # 일반 버스의 경우 범위 안의 모든 정류장 정차하므로 +1
                bus_stop[i] += 1

        elif bus == 2:                          # 광역버스는 짝수든 홀수든 2마다 정차하므로 해당 조건 줘서 +1
            for i in range(A+2 ,B, 2):
                bus_stop[i] += 1

        else:                                   # 광역급행버스
            if A % 2 == 0:                      # 짝수의 경우
                for i in range(A+1, B):
                    if i % 4 == 0:              # 4의 배수이면 정류장에 +1
                        bus_stop[i] += 1
            else:                               # 홀수의 경우
                for i in range(A+1, B):         
                    if i % 3 == 0 and i % 10 != 0:   # 3의 배수이면서 10의 배수가 아니면 +1
                        bus_stop[i] += 1
    
    print(f'#{tc} {max(bus_stop)}')             # 카운트 리스트 중 가장 큰 값 출력
                                                # 값이 아닌 인덱스 번호를 추출하라는 문제가 나오면 어떻게 할지 고민해보기
                
