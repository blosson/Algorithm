# <IDEA>
# 1. brown과 yellow의 개수를 알면 가로, 세로의 길이를 방정식으로 구할 수 있다. 그렇지만 어떻게 프로그래밍으로 구현할까?
#     x + y = brown / 2 + 2
#     x-2 * y-2 = yellow
# 2. 가로, 세로의 길이는 최소 3이상이므로 i, j를 for문을 돌려 조건을 확인하여 확인


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
            break``

    return answer
