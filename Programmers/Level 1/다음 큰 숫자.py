# <IDEA>
# 1. while문으로 n+1 부터 시작
# 2. bin 함수를 사용하여 1의 개수를 카운트하고 같은지 확인. 같다면 return

def solution(n):
    n_cnt = bin(n)[2:].count('1')

    answer = n+1
    while True:
        if bin(answer)[2:].count('1') == n_cnt:
            return answer
        else:
            answer += 1