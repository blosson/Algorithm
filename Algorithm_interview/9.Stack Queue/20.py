# 괄호검사
example = input()

stack = []
ans = True

for i in example:                   
    if i == '(' or '{' or '[':      # 왼쪽 괄호들일 경우 일단 무조건 push
        stack.append(i)
    else:                           # 오른쪽 괄호들일 경우
        if i == ')':                
            if stack[-1] == '(':    # 마지막으로 push한 값이 짝이 맞으면 stack에서 pop
                stack.pop()
            else:                   # 아니면 알맞은 괄호쌍이 아니므로 ans = False로 바꿔주고 for문 종료
                ans = False
                break
        if i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                ans = False
                break
        if i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                ans = False
                break


if stack:                           # push했던 왼쪽 괄호들이 남아있으면 잘못된 쌍이므로 ans = False
    ans = False

print(ans)


        