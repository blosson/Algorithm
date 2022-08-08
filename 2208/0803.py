test_case = int(input()) # 테스트 케이스 입력

case_number = 1
while case_number <= test_case: # 반복

    number = list(map(int, input().split())) # 두 정수 입력(A, B)

    count = 0
    for i in range(number[0], number[1]+1): # A이상 B이하의 수를 차례대로 반복
        i_str = str(i) # int->str 변경 (팰린드롬인지 확인 위해)
        if i_str == i_str[::-1]: # 팰린드롬 확인
           root = i ** (1/2) # 루트값 확인
           if root == int(root): # 제곱근이 정수면
                root_str = str(int(root))
                if root_str == root_str[::-1]: # 제곱근과 거꾸로 값이 같으면
                    count = count + 1
    
    print(f'#{case_number} {count}')
    case_number = case_number + 1

# 실수에 int를하면 소수점 아래값이 사라진다! 이제 앎...

