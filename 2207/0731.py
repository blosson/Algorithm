
case = int(input())

for i in range(case):
    num = list(map(int, input('10개의 수를 입력하세요. : ').split()))  # map 함수 다시 공부하기
    
    del num[0] # 첫 인덱스 삭제
    del num[-1] # 마지막 인덱스 삭제
    
    
    num_sum = sum(num)
    num_average = round(sum(num) / len(num)) # 평균구하고 첫째 자리에서     반올림하여 정수로 만듦
    print(f'#{i+1} {num_average}')

