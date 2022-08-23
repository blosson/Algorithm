for tc in range(1, int(input()) + 1):  
    str1 = input()
    stack = []
    ans = ''

    for char in str1:                               # 전체 문자열 순회
        if char in '+-*/':                          # 연산자의 경우
            if not stack:                           # 비어있으면 무조건 stack에 넣어줌
                stack.append(char)
            else:                                   # 안 비어있는 경우
                if char in '*/':                    # 곱셉/나눗셈의 경우
                    while True:
                        if stack[-1] in '*/':       # stack[-1]에 같은 순서 연산자가 있으면
                            ans += stack.pop()      # pop해서 후위표기법 결과값에 추가
                        else:
                            break
                    stack.append(char)              # 자기보다 센 연사자 더 이상 없으면 stack에 추가

                else: # +-                          # 덧셈/뺄셈의 경우
                    while True:
                        if stack[-1] in '+-':       # stack[-1]에 같은 순서 연산자가 있으면 222
                            ans += stack.pop()      # pop해서 후위표기법 결과값에 추가 222
                        else:
                            break
                    stack.append(char)              # 자기보다 센 연사자 더 이상 없으면 stack에 추가 222

        else:                                       # 피연산자는 그냥 결과값에 추가
            ans += char                             # string 끼리도 이렇게 더할 수 있다!!!!

    while 1 <= len(stack):                          # stack에 있는 남은 피연산자들을 while문을 통해 모두 후위표기법에 추가해줌
        ans += stack.pop()

    print(f'#{tc} {ans}')


# 후위표기법 토대로 계산하기
'''back_str = '6528-*2/+'
stack = []

for char in back_str:
    if char in '+-*/':
        if char == '+':
            char1 = int(stack.pop())
            char2 = int(stack.pop())
            cal = char2 + char1
            stack.append(cal)
        if char == '-':
            char1 = int(stack.pop())
            char2 = int(stack.pop())
            cal = char2 - char1
            stack.append(cal)
        if char == '*':
            char1 = int(stack.pop())
            char2 = int(stack.pop())
            cal = char2 * char1
            stack.append(cal)
        if char == '/':
            char1 = int(stack.pop())
            char2 = int(stack.pop())
            cal = char2 / char1
            stack.append(cal)

    else:
        stack.append(char)

ans = stack.pop()
print(ans)'''
        