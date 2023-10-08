# <IDEA>
# 피보나치 형태로 정답이 출력된다! → 이 순서를 발견 못했으면 어떻게 풀어야 했을지 감이 안 옴

#1 DP 풀이
def solution(n):
    def jump(n):
        jump_list = [0, 1, 2]
        for i in range(3, n+1):
            # DP를 활용하여 중복 계산 피하기
            jump_list.append(jump_list[i-2] + jump_list[i-1])
            # print(jump_list)
        return jump_list[n]
    
    answer = jump(n) % 1234567
    return answer



#2 일반 재귀 풀이 (시간초과) - 같은 함수 반복 호출 때문
def solution(n):
    def jump(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return jump(n-1) + jump(n-2)
                                
    answer = jump(n) % 1234567
    return answer