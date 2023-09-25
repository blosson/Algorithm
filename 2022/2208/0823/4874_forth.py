for tc in range(1, int(input()) + 1):  

    code = list(input().split())
    stack = []

    for c in code:
        if c not in '+-*/':                         
            if c != '.':                              # 숫자일 때
                stack.append(int(c))
            else:                                     # '.' 일 때
                if len(stack) != 1:                   # stack 길이가 2보다 길면 error
                    ans = 'error'
                    break
                else:                                 # 나머지는 정답 출력
                    ans = stack.pop()

        else:                                         # 연산자일 경우
            if len(stack) >= 2:                       # stack 길이가 2보다 크면 진행
                c1 = stack.pop()
                c2 = stack.pop()

                if c == '+':
                    cal = c2 + c1
                elif c == '-':
                    cal = c2 - c1
                elif c == '*':
                    cal = c2 * c1
                if c == '/':
                    cal = c2 // c1                    # int(c2 / c1) 이렇게도 됨 나눗셈할 때 int 진짜 조심하자
                
                stack.append(cal)

            else:                                     # 작으면 error
                ans = 'error'
                break

    print(f'#{tc} {ans}')
        

