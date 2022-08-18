# M*N에서 회문이 있는지 확인하는 코드 (문제 잘못 읽고 삽질해서 여기에 시간 날림 ㅠ)
T = int(input())
for tc in range(1, T+1):

    M, N = list(map(int, input().split()))
    letters = [list(input()) for _ in range(M)]


    for k in range(M):
        if letters[k] == letters[k][::-1]:  # list[k] == list[k][::-1] 2차원 리스트 회문 확인 방법
            ans_row = ''.join(letters[k])
            print(f'#{tc} {ans_row}') # join으로 붙이기
            break


    for j in range(N):
        test_list = []
        for i in range(M):
            test_list.append(letters[i][j])
        if test_list == test_list[::-1]:
            ans_col = ''.join(test_list)
            print(f'#{tc} {ans_col}')
            break