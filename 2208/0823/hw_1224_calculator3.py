for tc in range(1, 11):
    int(input())
    code = input()

    stack = []
    postfix = ''
    for c in code:
        if c in '()*+':                                                     # 연산자 or 괄호일 때
            if c == '(':                                                    # 여는 괄호면 무조건 push
                stack.append(c)
            elif c == '*':                                                  # *면 stack이 비어있지 않고 top의 *를 pop해준 뒤에 push
                while stack and stack[-1] == '*':                           # stack and 가 꼭 들어가야함을 주의!
                    postfix += stack.pop()
                stack.append(c)
            elif c == '+':                                                  # +면 stack이 비어있지 않고 top의 *, +를 pop해준 뒤에 push
                while stack and (stack[-1] == '*' or stack[-1] == '+'):
                    postfix += stack.pop()
                stack.append(c)
            else: # )일 경우                                                # 닫는 괄호면 여는 괄호가 될 때까지 연산자들을 pop 해줌
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()                                                 # top에 위치한 여는 괄호는 pop만 하고 append 하지 않음
        else:
            postfix += c

    while len(stack) >= 1:                                                  # stack에 남아있는 것들을 while문 돌려서 다 postfix에 넣어줌
        postfix += stack.pop()

    stack = []                                                              # 계산 시에 사용할 빈 stack (근데 사실 stack이 비어있으니 초기화 해줄 필요 없을듯)
    for char in postfix:
        if char not in '+*':                                                # postfix에는 ()가 없으니 굳이 안 넣어줘도 됨
            stack.append(int(char))
        else:
            char1 = stack.pop()                                             # 하나 먼저 pop해서 변수로 만들어줌
            if char == '+':
                cal = stack.pop() + char1                                   # 이런식으로 하면 안 헷갈리고 연산 가능
            elif char == '*':
                cal = stack.pop() * char1
            stack.append(cal)
    ans = stack[-1]                                                         # stack[-1] 값이 최종 계산값
    print(f'#{tc} {ans}')


        