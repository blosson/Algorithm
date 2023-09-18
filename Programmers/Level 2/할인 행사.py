# <Idea>
# 1. discount 배열을 10개씩 끊어 순회
# 2. 10개 중 물품이 나올 때마다 want 목록에 있으면 number[i]를 -1씩 해줌
#     - number 배열 복사
# 3. sum(num)이 0이면 result +1

# .copy()
# from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # want, number를 key, value로 하는 딕셔너리 생성
    wish_dict = {}
    for key, value in zip(want, number):
        wish_dict[key] = value
        
    # dicount 리스트를 10개씩 끊어서 순회
    for i in range(len(discount) - 9):
        items = discount[i:i+10] 
        
        # wish_dict 복사, 할인 목록 순회해서 존재하면 복사한 dict의 value를 -1 해줌 
        wish_copy = wish_dict.copy()
        for item in items:
            if item in wish_copy:
                wish_copy[item] -= 1
            else:
                break
        
        # 각 복사한 wish_copy의 value들의 합이 0이면 회원가입하므로 is_pass를 True로 유지
        is_pass = True
        for key in wish_copy:
            if wish_copy[key] == 0:
                pass
            else:
                is_pass = False
                break
        
        if is_pass == True:
            answer += 1                       
    
    return answer