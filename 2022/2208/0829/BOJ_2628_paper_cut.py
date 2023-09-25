width, height = map(int, input().split())                           # 너비, 높이 (너비가 열, 높이가 행임에 주의!)
N = int(input())
cut_list = [list(map(int, input().split())) for _ in range(N)]      # 자를 부분 입력

cut_width = []                                                      # 열을 자를 위치를 담을 리스트
cut_height = []                                                     # 행을 자를 위치를 담을 리스트
for cut in cut_list:
    if cut[0] == 0:                                                 # 행을 자르면 cut_height에 추가
        cut_height.append(cut[1])
    else:                                                           # 열을 자르면 cut_width에 추가
        cut_width.append(cut[1])

cut_width.append(width)                                             # 추후 계산을 위해 가로와 세로의 최대 길이도 리스트에 추가
cut_height.append(height)

cut_width.sort()                                                    # 추후 계산을 위해 정렬
cut_height.sort()


area_list = []                                                      # 구분된 각 넓이를 담을 리스트 생성
for i in range(len(cut_height)):                                    # 두 리스트를 돌면서 
    for j in range(len(cut_width)):
        if i == 0 and j == 0:                                       # i, j index가 0이면 index[0] 값끼리 곱해줌 (넓이 계산 위해)
            area_list.append((cut_height[i]) * (cut_width[j]))
        elif i == 0 and j != 0:                                     # 둘 중 하나만 0이면 0이 아닌 값은 그 전 인덱스 값을 빼준 뒤 곱해줌
            area_list.append((cut_height[i]) * (cut_width[j] - cut_width[j-1]))
        elif i != 0 and j == 0:                     
            area_list.append((cut_height[i] - cut_height[i-1]) * (cut_width[j]))
        else:                                                       # 둘 다 0이 아니면 자신의 인덱스 값과 그 전 인덱스 값을 빼준 뒤 서로 곱해줌
            area_list.append((cut_height[i] - cut_height[i-1]) * (cut_width[j] - cut_width[j-1]))
        
ans = max(area_list)                                                # 해당 리스트에서 최댓값 출력 (= 최대 넓이)
print(ans)    