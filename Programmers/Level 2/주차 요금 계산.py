# <Idea>
# 1. fees 요소들 각 변수에 저장, records 순회해서 공백 기준으로 split해서 각 변수에 저장
# 2. 주차 요금 계산
#     - 기본 시간과 일치하는 경우 추가 요금 없음(초과시에만 계산)
#     - 두번 입차하는 경우에 기본시간은 1번만 적용, 기본 요금도 1번만 적용
#     - 입차만 있고 출차내역이 없는 경우 23:59로 계산
#     - 차량 번호 오름차순 정렬
#     - 시간-분 계산 어떻게 할지
#         - 각 차량번호 별로 key-value로 하는 dict 생성
#         1. 각 차량 번호별 value 순회 (만약 길이가 홀수면 23:59를 append)
#         2. :기준으로 split 해서 시간은 시간끼리, 분은 분끼리 빼기
#         3. 시간 * 60을 해주고 분과 더해줌
   

def solution(fees, records):
    # fees 요소들 각 변수에 저장
    basic_time = fees[0]
    basic_charge = fees[1]
    unit_time = fees[2]
    unit_charge = fees[3]
    
    # 차량별 출입 현황 split해서 dict에 넣어줌
    parking_info = {}
    for record in records:
        info = record.split(' ')
        time, car_num, parking_type = info[0], info[1], info[2]
        if car_num in parking_info:
            parking_info[car_num].append(time)
        else:
            parking_info[car_num] = [time]
        # print(parking_info)
        
    # 차량 번호 순서대로 오름차순 정렬 (dict -> list -> dict)
    parking_list = sorted(parking_info.items())
    parking_info = {}
    for info in parking_list:
        parking_info[info[0]] = info[1]
    
    answer = []
    # 이미 오름차순 정렬했으므로 차량번호인 key없이 values만 가져와도 됨
    for infos in parking_info.values():
        # infos 길이가 홀수라면 출차기록이 없다는 뜻이므로 23:59를 추가
        if len(infos) % 2 == 1:
            infos.append('23:59')
        
        # 각 in-out 시간-분으로 쪼개기 (2 간격만큼 순회)
        total_time = 0
        for i in range(0, len(infos), 2):
            in_hour, in_min = int(infos[i].split(':')[0]), int(infos[i].split(':')[1])
            out_hour, out_min = int(infos[i+1].split(':')[0]), int(infos[i+1].split(':')[1])
            
            # 누적 주차시간 계산
            total_time += (out_hour - in_hour) * 60 + (out_min - in_min)

        
        # 주차시간이 기본 주차시간 보다 작으면 단위요금 부과할 시간 0
        if total_time - basic_time <= 0:
            charge_time = 0
        # 딱 나누어 떨어지면 몫만큼만 곱할 시간
        elif (total_time - basic_time) % unit_time == 0:
            charge_time = int((total_time - basic_time) / unit_time)
        # 나누어 떨어지지 않으면 올림해서 몫+1 만큼 요금 계산
        else:
            charge_time = (total_time - basic_time) // unit_time + 1
        
        # 최종 요금 = 기본 요금 + (단위시간수 * 단위요금)
        final_price = basic_charge + (charge_time * unit_charge)
        answer.append(final_price)
        
    return answer