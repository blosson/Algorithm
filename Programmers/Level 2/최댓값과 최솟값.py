# <IDEA>
# 1. ' ' 기준으로 split하고, map 함수를 사용해 int로 바꿔줌
# 2. 최솟값과 최댓값을 str로 만들어 ' '을 가운데에 두고 연결

def solution(s):
    numbers = list(map(int, s.split(' ')))
    # print(numbers)
    min_num, max_num = str(min(numbers)), str(max(numbers))
    answer = min_num + ' ' + max_num
    return answer