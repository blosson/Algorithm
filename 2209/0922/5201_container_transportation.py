import sys
sys.stdin = open('5201.txt', 'r')

for tc in range(1,int(input()) + 1):
    
    N, M = map(int, input().split())
    con_weight = list(map(int, input().split()))
    truck_capacity = list(map(int, input().split()))

    con_weight = sorted(con_weight, reverse=True)                   # 화물무게와 트럭적재용량을 각각 내림차순으로 정렬 (이후 편하게 계산하기 위해)
    truck_capacity = sorted(truck_capacity, reverse=True)


    if con_weight[-1] > truck_capacity[0]:                          # 화물의 최소무게가 트럭의 최대 적재용량보다 적으면 실을 수 없으므로 ans = 0
        ans = 0

    else:
        ans = 0
        for container in con_weight:                                # 각 컨테이너의 무게 별로 실을 수 있는 트럭이 있는지 순회하면서 체크
            for truck in truck_capacity:                            
                if container > truck:                               # truck이 내림차순 정렬되어 있으므로 컨테이너 > 첫 트럭 이면 불가능하므로 안쪽 for문 종료
                    break
                else:                                               
                    ans += container                                # 적재가능하다면 해당 컨테이너 무게 ans에 더해주고
                    truck_capacity.pop(0)                           # B도시로 떠난 트럭은 안녕.. pop(0)로 제거해줌
                    break                                           # 화물을 실었으니 이후 트럭은 순회할 필요 없이 break

    print(f'#{tc} {ans}')

            