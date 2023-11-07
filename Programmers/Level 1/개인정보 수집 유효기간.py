# 문제 조건 제대로 안 읽었다가 3시간 썼다..
# split, map 함수

def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜에서 '.'을 제거하고 숫자로 변경
    today = int(today.replace('.', ''))
    
    for idx, privacy in enumerate(privacies, 1):
        for term in terms:
            # 유효기간 문자가 같으면, 시작날짜에서 '.'을 제거하고 숫자형태로 바꿈
            if privacy[-1] == term[0]:
                start = privacy[:10].replace('.', '')
                
                # index 2번부터 끝까지가 + 유효기간 (전에는 2자리까지밖에 생각 안해서 19번 TC가 틀렸던 거)
                term_month = int(term[2::])
    
                # 더해진 후 월 숫자 (12 초과 가능)
                my_month = int(start[4:6]) + term_month
                
                # 12월인 경우에는 아직 해가 지나지 않았으므로 -1을 해주고 그렇지 않으면 몫만큼 년에 더해준다
                if my_month % 12 == 0:
                    plus_year = (my_month // 12) - 1
                else:
                    plus_year = (my_month // 12)
                new_year = int(start[:4]) + plus_year 
                
                # 1~9월까지는 앞에 0을 붙여주고, 나머지가 0은 12월이므로 따로 조건 분리
                plus_month = my_month % 12
                if plus_month == 0:
                    new_month = '12'
                elif plus_month < 10:
                    new_month = '0' + str(plus_month)
                else:
                    new_month = str(plus_month)
                
                end = int(str(new_year) + new_month + start[-2::])
                
                # 오늘 날짜가 만료일보다 같거나 같으면 리스트에 추가 (이미 정렬되어있으므로 정렬 필요 X)
                if today >= end:
                    answer.append(idx)      

    return answer