rec1 = list(map(int, input().split()))          # 각 사각형 좌표 입력 (x1, y1, x2, y2)
rec2 = list(map(int, input().split()))          # (왼쪽 아래부터 오른쪽 위 순서)
rec3 = list(map(int, input().split()))
rec4 = list(map(int, input().split()))

coordinate = [[0] * 101 for _ in range(101)]    # 전체 x, y 좌표 생성 

for i in range(rec1[0], rec1[2]):               # 첫 번째 사각형 좌표만큼 좌표에 채워줌
    for j in range(rec1[1], rec1[3]):
        coordinate[i][j] += 1

for i in range(rec2[0], rec2[2]):
    for j in range(rec2[1], rec2[3]):
        coordinate[i][j] += 1

for i in range(rec3[0], rec3[2]):
    for j in range(rec3[1], rec3[3]):
        coordinate[i][j] += 1

for i in range(rec4[0], rec4[2]):               # 같은 작업 4번째 사각형까지 반복
    for j in range(rec4[1], rec4[3]):
        coordinate[i][j] += 1

sum_all = 0                                             # 중복포함 전체 넓이 계산
for i in range(101):
    for j in range(101):
        sum_all += coordinate[i][j]

del_duplication = 0                                     # 중복값 계산
for i in range(101):
    for j in range(101):
        if coordinate[i][j] >= 2:                       # 해당 좌표값이 2 이상이면
            del_duplication += (coordinate[i][j] - 1)   # 해당 값에서 1을 빼준 값을 변수에 넣어줌 (중복되는 넓이)

ans = sum_all - del_duplication                         # 중복넓이 - 중복값 = 정답
            
print(ans)




