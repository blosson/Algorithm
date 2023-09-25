for tc in range(1, 11): 
    
    int(input())
    word = input()

    stack = []
    postfix = ''
    for w in word:                 
        if w in '+*':
            if not stack:
                stack.append(w)
            else:
                if w == '+':
                    while stack and stack[-1] in '*+': # stack을 해줘야 빈 값이 있을 때 [-1]을 하지 않아서 오류가 안 남
                        postfix += stack.pop()

                    stack.append(w)
                else:
                    while stack and stack[-1] in '*': 
                        postfix += stack.pop()

                    stack.append(w)

        else:
            postfix += w

    while 1 <= len(stack):
        postfix += stack.pop()

    stack = []
    for char in postfix:
        if char == '*':
            char1 = int(stack.pop())
            char2 = int(stack.pop())
            cal = char2 * char1
            stack.append(cal)
        elif char == '+':
            char1 = int(stack.pop())
            char2 = int(stack.pop())
            cal = char2 + char1
            stack.append(cal) 

        else:
            stack.append(char)

    ans = stack.pop()
    print(f'#{tc} {ans}')