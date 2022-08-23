for tc in range(1, int(input()) + 1):  

    code = list(input().split())

    stack = []
    for c in code:
        if c not in '+-*/':                         
            if c != '.':                                  # 숫자일 때
                stack.append(c)
            else:                                         # '.' 일 때
                if not stack:           
                    print(f'#{tc} error')                 # stack에 암것두 없으면 error
                    break
                else:
                    if len(stack) != 1:                   # stack 길이가 2보다 길면 error
                        print(f'#{tc} error')
                        break

                    else:                                 # 나머지는 정답 출력
                        ans = stack.pop()
                        print(f'#{tc} {ans}')

        else:                                             # 연사자일 경우
            if c == '+':                    
                if len(stack) >= 2:                       # stack 길이가 2 이상일 경우
                    if stack[-1] not in '+-*/' and stack[-2] not in '+-*/': # 인덱스 -1, -2가 연산자가 아니면
                        c1 = int(stack.pop())             # int로 변환하여 계산
                        c2 = int(stack.pop())
                        cal = str(c2 + c1)                # in을 쓰기 위해 다시 str으로 변환
                        stack.append(cal)                 # 연산하여 stack에 추가
                    else:
                        print(f'#{tc} error')
                        break        
                else:
                    print(f'#{tc} error')
                    break

            if c == '-':
                if len(stack) >= 2:
                    if stack[-1] not in '+-*/' and stack[-2] not in '+-*/':
                        c1 = int(stack.pop())
                        c2 = int(stack.pop())
                        cal = str(c2 - c1)
                        stack.append(cal)
                    else:
                        print(f'#{tc} error') 
                        break       
                else:
                    print(f'#{tc} error')
                    break

            if c == '*':
                if len(stack) >= 2:
                    if stack[-1] not in '+-*/' and stack[-2] not in '+-*/':
                        c1 = int(stack.pop())
                        c2 = int(stack.pop())
                        cal = str(c2 * c1)
                        stack.append(cal)
                    else:
                        print(f'#{tc} error') 
                        break     
                else:
                    print(f'#{tc} error')
                    break

            if c == '/':
                if len(stack) >= 2:
                    if stack[-1] not in '+-*/' and stack[-2] not in '+-*/':
                        c1 = int(stack.pop())
                        c2 = int(stack.pop())
                        cal = str(c2 / c1)
                        stack.append(cal)
                    else:
                        print(f'#{tc} error')  
                        break      
                else:
                    print(f'#{tc} error')
                    break
        

