
test_case = int(input())

for i in range(1, test_case):
    numbers = map(int, input().split()) # 10개 숫자 받기
    numbers_list = list(numbers) # list로 변환(정렬하여 제거하기 위해)

    numbers_list.sort() # 정렬(원본 변함)

    del numbers_list[0] # 젤 낮은 수 제거
    del numbers_list[-1] # 젤 높은 수 제거

    sum_numbers = sum(numbers_list) # 리스트 다 더해~~~(리스트도 sum 되네..)
    average_numbers = sum_numbers / len(numbers_list) # 평균 구하기


    round_average_numbers = round(average_numbers) # round 조건 없으면 소수점 1의 자리에서 반올림!
    print(f'#{i} {round_average_numbers}')
