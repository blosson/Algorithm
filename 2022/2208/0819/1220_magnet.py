import sys
sys.stdin = open('1220.txt', 'r')

for tc in range(1, 11):
    length = int(input())
    table = list(list(map(int, input().split())) for _ in range(100))

    cnt_sum = 0                                     # 전체 몇개인지 (정답)
    for j in range(100):                            # 행은 생각할 필요가 없기 때문에 열만 생각 (사실 행열 바꾸는 법 모름..)

        stack = []                                  # 빈 스텍 생성 
        for i in range(100):
            if table[i][j] == 2:                    # 2일 경우 (위로 붙는 거) 
                if not stack:                       # 스택이 비어있으면 아래로 떨어지기 때문에 pass
                    pass
                elif stack[-1] == 1:                # 앞에 1이 있거나 2가 있으면 그냥 추가해줌
                    stack.append(table[i][j])
                else:
                    stack.append(table[i][j])

            if table[i][j] == 1:                    # 1일 경우 (아래로 붙는 거)
                stack.append(table[i][j])           # 일단 다 추가

        while True:                                 # 1이 스택 가장 마지막에 있을 경우에는 아래로 떨어지기 때문에
            if stack and stack[-1] == 1:            # while문과 pop을 통해 다 제거해준다.
                stack.pop()
            else:
                break
            
        cnt = 0                                     # 한 열에 몇개인지
        test_list = [1, 2]                          # 테스트용 리스트 / stack 안에 1, 2가 반복되는 만큼이 교착상태의 개수!
        for k in range(len(stack) - 1):
            if stack[k:k+2] == test_list:           # 1, 2가 있는 만큼
                cnt += 1                            # cnt에 추가
        cnt_sum += cnt                              # cnt_sum에 추가 

    print(f'#{tc} {cnt_sum}')
            
        

    
    
                
           
                
            