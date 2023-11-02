# <IDEA>
# 1. str 메서드를 활용해서 0의 갯수를 센 뒤 0을 모두 제거 (count, replace)
# 2. 남은 str의 길이를 재서 이진법으로 변환
# 3. 1이 될 때까지 반복하고 횟수와 제거된 0의 갯수를 세줌

# bin함수를 쓰면 십진수 → 이진수 변환이 가능하다!

# - 다만, 1번 idx까지는 0b가 나오니 알아서 슬라이싱 해서 잘 쓰도록 하자
# >>> bin(10)
# '0b1010'


def solution(s):
    cnt = 0             # 이진 변환 횟수
    zero_cnt = 0        # 제거된 0의 개수

    while True:      
        if s == '1':    # 종료 조건
            break
        
        cnt += 1                    # 이진 변환 시마다 +1
        zero_cnt += s.count('0')    # 제거될 0 개수 +
    
        s = s.replace('0', '')
        s_len = len(s)
        
        bi_cnt = 0                              # 이진수 자리수 계산
        while s_len >= 2 ** bi_cnt:
            if s_len >= 2 ** (bi_cnt + 1):
                bi_cnt += 1
            else:
                break
        
        s = ''                                  # 이진수 변환
        for i in range(bi_cnt, -1, -1):
            if s_len >= 2 ** i:
                s += '1'
                s_len -= 2 ** i
            else:
                s += '0'

    answer = [cnt, zero_cnt]
    return answer