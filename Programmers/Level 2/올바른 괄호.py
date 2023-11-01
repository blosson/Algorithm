def solution(s):
    answer = False
    
    stack = []
    for blank in s:
        if blank == "(":                # 좌측 괄호면 stack에 넣기
            stack.append(blank)
            
        else:                           # 우측 괄호면 stack이 비어있거나 바로 앞이 (가 아니면 올바른 괄호가 아님
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return answer
                    
            else:
                return answer    
    
    if not stack:
        answer = True
        
    return answer