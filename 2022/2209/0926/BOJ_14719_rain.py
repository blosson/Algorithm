'''어떻게 빗물의 양을 구할 수 있을까에 대한 고민?

1번 방법
1) 양쪽 끝 값들이 사이에 있는 값들보다 커야 빗물이 고임
2) 그렇지 않다면그 구간을 조사해서 찾아보기
3) 근데 어떻게 구현해야할지 모르겠음 -> 포기

2번 방법
1) 높이의 max를 찾고 양쪽을 탐색
2) 조건들과 edge case가 너무 많이 생각남 -> 포기

결국 구글 형님의 힘을 빌렸다..
1번 방법에서 해당 인덱스 값만 더해주는 식으로 했으면 됐는데 넘나리 아쉽..
조금만 더 생각해볼걸'''


H, W = map(int, input().split())
blocks = list(map(int, input().split()))

for _ in range(1):                                          # 바로 종료되는 다양한 조건이 있겠지만 일단 생각할 수 있는 것만 해보았다.
    if blocks.count(0) == W or blocks.count(0) == W-1:      # 전부다 0이거나, 하나 빼고 전부 0이면 아래 for문을 돌 것도 없음.
        cnt = 0                                             
        break
    
    cnt = 0                                                 # 빗물의 양      
    for i in range(1, W-1):                                 # 자신을 기준으로 왼쪽 오른쪽 값이 더 커야 빗물이 고이므로
        left_max = max(blocks[:i])                          # 양쪽에서 max값을 구해준 뒤 두 max 중 작은 값을 골라준다.
        right_max = max(blocks[i+1:])
        lower_height = min(left_max, right_max)             
        
        if blocks[i] < lower_height:                        # 현재 높이보다 lower_height가 더 크면 그 차만큼이 빗물이 고일 수 있는 양임
            cnt += (lower_height - blocks[i])

print(cnt)

# 아 코드는 이렇게 간단한데 생각해내기가 왜 이렇게 어렵지 아럼대ㅔ럳ㅁ재ㅑ럳ㅈㅁ;ㅏㅣ룯미ㅓㅏㄹ무래ㅑㅕㅂㄷ절;ㅐㄷㅁㅈ럼ㅈ디ㅑ롬ㅈ대;렂ㄷ매;ㄹ
        
        


