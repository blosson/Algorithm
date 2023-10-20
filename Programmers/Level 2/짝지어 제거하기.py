# <IDEA>
# - 문자열의 길이가 10억까지니까 실제로 해당 과정을 거치는 것이 아니라 해당 과정이 가능한지 판별하는 것이 핵심
# - stack을 사용한다!! 이 개념이 떠오르지 않아서 고생을 했다.

def solution(s):
    answer = 0

    stack = []          # stack 생성
    for i in s:
        if stack and i == stack[-1]:    # 순회하며 현재 문자가 stack의 마지막 인덱스 값과 같으면 pop()
            stack.pop()
        else:                           # 아니라면 stack에 추가
            stack.append(i)
    
    if not stack:       # stack에 비어있으면 짝지어 제거하기 성공이니 answer=1로 변경
        answer = 1
    return answer