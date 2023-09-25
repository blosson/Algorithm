for tc in range(1, int(input()) + 1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    TF = True
    for i in range(9):
        if set(sudoku[i]) == test_set:
            pass
        else:
            TF = False
            print(f'#{tc} 0')
            quit()
            


    for j in range(9):
        row_list = []
        for i in range(9):
            row_list.append(sudoku[i][j])
        if set(row_list) == test_set:
            pass
        else:
            TF = False
            print(f'#{tc} 0')
            quit()


    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            box_list = []
            for a in range(3):
                for b in range(3):
                    box_list.append(sudoku[k+a][l+b])
            if set(box_list) == test_set:
                pass
            else:
                TF = False
                print(f'#{tc} 0')
                quit()


    if TF == True:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
