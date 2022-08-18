paren = input()                                     # 괄호 입력

def parenthesis(paren):                             
    test_list = []                                  # 테스트용 빈 list
    for i in paren:     
        if i == '(':                                # 왼쪽괄호는 일단 추가
            test_list.append(i)
        elif i == ')':      
            if test_list == []:                     # 오른쪽 괄호인데 빈 list일 경우
                return "what's wrong with you?"     # 삐빅~
            else:
                test_list.pop()                     # 아니면 그냥 pop 해서 삭제
    
    if test_list == []:                             # for문 끝낸 뒤 빈 list면
        return 'succes'                             # 성공~
    else:
        return "what's wrong with you?"             # 실패~

print(parenthesis(paren))
            
