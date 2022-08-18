'''import sys
sys.stdin = open('1216.txt', 'r')

for tc in range(1, 11):
    abc = [list(input()) for _ in range(100)]

    rowmax_len = 0
    for i in range(100):
        for j in range(100): # 각 칸
            for k in range(100-j):
                abc_row = abc[i][j:j+k]     # 어차피 최소 1 이상이므로 빈 리스트는 일단 그냥 두자
                if abc_row == abc_row[::-1]:
                    row_len = len(abc_row)
                    if row_len > rowmax_len:
                        rowmax_len = row_len


    for a in range(100):
        for b in range(100):
            abc_col = []
            for c in range(100-b):
                abc_col.append(abc[a][b+c])
                if abc_col == abc_col[::-1]: 
                    col_len = len(abc_col)
                    if col_len > colmax_len:
                        colmax_len = col_len

    if rowmax_len >= colmax_len:
        print(f'#{tc} {rowmax_len}')
    else:
        print(f'#{tc} {colmax_len}')'''

# 다른 분 코드 활용 ()

def mymax(a,b): # 최댓값 구하기 함수
    if a > b:
        return a
    return b

def findleng(arr): # 최대 길이 구하기
    max_leng = 0
    for row in arr: # 행 마다 체크
        for i in range(100): # 시작 지점
            for j in range(100,-1,-1): # 끝지점
                if j-i+1 > max_leng: # 필요없는 경우 제외
                    word = row[i:j]
                    if word == word[::-1]: # 회문이면
                        leng = len(word)
                        max_leng = mymax(max_leng, leng) # 업데이트
                        break
    return max_leng

for _ in range(10):
    TC = int(input())
    grid = [list(input()) for _ in range(100)] # 행 체크
    grid_rev = [[grid[j][i] for j in range(100)] for i in range(100)] # 열 체크
    max_row = findleng(grid)
    max_col = findleng(grid_rev)
    max_val = mymax(max_row, max_col)

    print(f'#{TC} {max_val}')
            
            