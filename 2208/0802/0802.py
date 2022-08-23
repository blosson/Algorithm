test_case = int(input())

for case in range(1, test_case + 1):
    num = int(input()) # 숫자 입력 받기
    num_str = str(num) # str로 변경(각 숫자를 분리하기 위해)
    num_set = set(num_str) # 중복값 없애기
    num_diversity = len(num_set) # 다양성 구하기 

    print(f'#{case} {num_diversity}')
