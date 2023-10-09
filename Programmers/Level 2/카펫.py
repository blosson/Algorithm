def solution(brown, yellow):
    answer = []
    # 가로:i, 세로:j, 가로 또는 세로는 3부터 가능함 (문제 조건)
    # 브루트포스 탐색
    for j in range(3, (int(brown/2))):
        # j값이 정해졌을 때 brown에 의해 자동적으로 i값도 정해짐
        i = int((brown / 2) + 2 - j)
        # print(i, j)
        # i, j 값이 노란색 박스 크기를 만족하는 조건에 해당하면
        if (i-2) * (j-2) == yellow:
            answer.append(i)
            answer.append(j)
            break

    return answer
