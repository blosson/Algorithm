number, count = map(int, input().split())
number_list = list(map(int, str(number)))       # 정수를 리스트로 변환


for _ in range(count):                          

    for i in range(len(number_list)):           # 리스트 순회하면서 확인

        max_num = max(number_list)              # 가장 큰 자릿수에서 가장 뒤에 있는 인덱스 구하기
        max_index = -1
        for j in range(len(number_list)):
            if number_list[j] == max_num:
                max_index = j
        
        
        if number_list[i] != max_index and i != max_index:                                      # 자릿수가 큰 곳부터 시작해서 숫자 바꿔주기
            number_list[i], number_list[max_index] = number_list[max_index], number_list[i]
            break
        
        else:                                   # 첫 자리가 이미 가장 큰 수 일 때 어떻게 해야할지 모르겠음..
            pass

                                                # 1) 숫자 비교가 아니라 교환 횟수가 남아서 어쩔 수 없이 교환해야하는 경우 
                                                # 2) 77777 같이 같은 숫자들에 대한 경우의 수를 어떻게 처리해야할지 모르겠다..
                                                
print(*number_list)

32888 가지고 있는 숫자

88832 이상적
82883 1번 바꾼거
88823 2번 바꾼거

모든 경우의 수 