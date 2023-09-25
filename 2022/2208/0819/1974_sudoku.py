# range도 슬라이싱 방법을 알면 좋을듯 3번째 값이 띄워서 가는 걸 확실히 알자!


for tc in range(1, int(input()) + 1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]   # 스도쿠 입력

    test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}      # 행, 열, 박스와 비교할 set
    TF = True                                   # 정답 출력을 위한 기준 변수

    for i in range(9):                          # 행
        if set(sudoku[i]) == test_set:          # 각 행 리스트의 set값이 test_set와 같으면 pass
            pass
        else:                           
            TF = False                          # 다르면 TF = False 처리해주고 해당 for문을 끝냄        
            break

# ★★★ break는 해당 for문만 멈춰주는 거라 한번에 프로그램을 끝내서 시간 단축을 하고 싶은데 어떻게 하면 좋을까요?
# 뭔가 함수로 만들어서 return으로 빠져나가도 될 것 같기도 하고..

    for j in range(9):                          # 열
        row_list = []                           # 같은 열에 있는 값들을 담아주기 위한 리스트
        for i in range(9):
            row_list.append(sudoku[i][j])       # 같은 열에 있는 값들 리스트에 담아주기
        if set(row_list) == test_set:
            pass
        else:
            TF = False
            break


    for k in range(0, 9, 3):                    # 박스
        for l in range(0, 9, 3):                # 작은 사각형 기준 [0][0] 인덱스를 기준으로 판단
            box_list = []                       # 같은 박스에 있는 값들은 담아주기 위한 리스트
            for a in range(3):
                for b in range(3):
                    box_list.append(sudoku[k+a][l+b])
            if set(box_list) == test_set:
                pass
            else:
                TF = False
                break


    if TF == True:                              # 최종 결과가 True라면 1, 반대의 경우 0 출력
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
