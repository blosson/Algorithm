# RUNTIME ERROR~~~~~~

def parenthesis(code):                             
    test_list = []                          # 테스트용 빈 list
    for i in code:     
        if i == '(':                        # 왼쪽 괄호는 일단 넣는다      
            test_list.append(i)

        elif i == '{':                      # 왼쪽 괄호는 일단 넣는다  
            test_list.append(i)

        elif i == ')':      
            if test_list[-1] == '{':        # 마지막 인덱스에 다른 괄호가 있으면
                return 0
            elif test_list == []:           # 빈 리스트면
                return 0
            else:                           # 같은 모양 왼쪽 괄호가 있으면
                test_list.pop()             # pop

        elif i == '}':                       
            if test_list[-1] == '(':        # 마지막 인덱스에 다른 괄호가 있으면222                     
                return 0
            elif test_list == []:
                return 0  
            else:
                test_list.pop() 
                
        else:                               # 기타 다른 문자, 공백이면
            pass                            # pass

    if test_list == []:                     # 빈 리스트면 1 return 
        return 1
    else:                                   # 이건 굳이 필요한지 모르겠다..
        return 0

for tc in range(1, int(input()) + 1):
    
    code = input()      
    ans = parenthesis(code)                           
    print(f'#{tc} {ans}')