word = input()

stack = []                          # 결과를 저장할 빈 stack 만들기
top = -1                            # 초기 top -1

for i in word:
    if top >= 0:                    # = stack 안에 값이 있으면
        if stack[top] == i:         # stack 젤 위 값이랑 현재 글자가 같으면 (근데 이건 그냥 stack[-1]로 하면 top을 줄 필요가 없을 것 같다.)
            top -= 1                # top 값을 -1 해주고
            stack.pop()             # pop해서 제일 위에 있는 값을 삭제한다!
        else:
            top += 1                # 값이 없으면 top에 1을 더해주고
            stack.append(i)         # append에 추가해서 다음값과 비교할 준비를 해준다.
    else:
        top += 1                    # stack이 비어있으면 더 받아야지 암암
        stack.append(i) 

print(len(stack))