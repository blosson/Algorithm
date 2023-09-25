K = int(input())

farm_area = []
for _ in range(6):
    farm_area.append(list(map(int, input().split())))

location_ew = []                        # 동서 방향의 위치 값 기록할 리스트
location_sn = []                        # 남북 방향의 위치 값 기록할 리스트
now_ew = 0                              # 동서 방향 출발지점
now_sn = 0                              # 남북 방향 출발지점

for i in farm_area:
    if i[0] == 1:                       # 동쪽 방향이면
        now_ew += i[1]                  # 방향이동해주고 (+)
        location_ew.append(now_ew)      # 위치를 리스트에 기록

    if i[0] == 2:                       # 서쪽 방향이면 이동 (-)
        now_ew -= i[1]
        location_ew.append(now_ew) 

    if i[0] == 3:                       # 남쪽 방향이면 이동 (+)
        now_sn += i[1]
        location_sn.append(now_sn) 

    if i[0] == 4:                       # 북쪽 방향이면 이동 (-)
        now_sn -= i[1]
        location_sn.append(now_sn) 

max_ew = max(location_ew)               # 동서방향 최댓값, 최솟값
min_ew = min(location_ew)
max_sn = max(location_sn)               # 남북방향 최댓값, 최솟값
min_sn = min(location_sn)

max_width = max_ew - min_ew             # 전체 큰 사각형의 가로 (동서)
max_height = max_sn - min_sn            # 전체 큰 사각형의 세로 (남북)

big_box = max_height * max_width        # 가장 큰 사각형의 넓이


####### 작은 박스 길이 구하는 게 ㄱ이 4가지 모양으로 달라져서 값이 안 나오네요 ㅠㅠㅠ
# 여기서부터는 틀린 코드
location_ew.remove(0)                    
location_sn.remove(0)

small_box_width = max_width - abs(location_ew[0] - location_ew[1])
small_box_height = max_height - abs(location_sn[0] - location_sn[1])
small_box = small_box_width * small_box_height

ans = K * (big_box - small_box)
print(ans)