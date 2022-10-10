for tc in range(1, int(input()) + 1):

    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    center_idx = N // 2                                     # 가운데 인덱스 번호

    farm_sum = []                                           # 수확 범위(마름모) 더해줄 리스트
    for i in range(N):

        if i < center_idx:                                  # 가운데 인덱스 기준 왼쪽이면
            farm_diff = abs(center_idx - i)                 # farm_diff 차이 구해줌 (사실 abs는 필요 없을듯)
            farm_sum += farm[i][farm_diff:N-farm_diff]      # 규칙따라 슬라이싱해서 리스트에 넣어줌 (차이만큼 앞뒤에서 슬라이싱 됨)
        
        elif i > center_idx:                                # 센터 기준 오른쪽
            farm_diff = abs(i - center_idx)
            farm_sum += farm[i][farm_diff:N-farm_diff]
        
        else:                                               # 센터는 한 줄 전부 더해줌
            farm_diff = 0
            farm_sum += farm[i]

    ans = sum(farm_sum)
    print(f'#{tc} {ans}')
