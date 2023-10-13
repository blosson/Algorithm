# <IDEA>
# 1. 공백, 숫자, 기호 쌍을 버리고 후보에 넣는다.
#     - str을 따로 검사하는 메서드가 있으면 좋을듯 (isappha())
#     - 대소문자 무시 → lower()
# 2. 자카드 유사도 검사
#     - 공집합 경우 예외처리
#     - 다중집합 고려… → 이게 key 포인트
#     - 배열 합치기
# 3. 마지막 계산
#     - 소수점 아래 버리기 - 1을 나눈 몫 구한 뒤 int 함수

#1 오답 (zip이 잘못됨)
def solution(str1, str2):
    arr1 = []  
    arr2 = []
    for i in range(len(str1) - 1):
        s = str1[i:i+2]
        if s.isalpha():
            s = s.lower()
            arr1.append(s)
    
    for i in range(len(str2) - 1):
        s = str2[i:i+2]
        if s.isalpha():
            s = s.lower()
            arr2.append(s)  
    # print(arr1, arr2)
    
    union_list = []
    for s1, s2 in zip(arr1, arr2):
        if s1 not in union_list:
            union_list.append(s1)
    
        if s2 not in union_list:
            union_list.append(s2)
    
    
    if len(union_list) == 0:
        return 65536
    

    intersection_cnt = 0
    union_cnt = 0
    for s in union_list:
        cnt1 = arr1.count(s)
        cnt2 = arr2.count(s)
        
        if cnt1 >= 1 and cnt2 >= 1:
            min_cnt = min(cnt1, cnt2)
            max_cnt = max(cnt1, cnt2)
            
            intersection_cnt += min_cnt
            union_cnt += max_cnt
        
        else:
            max_cnt = max(cnt1, cnt2)
            union_cnt += max_cnt
    
    similarity_percent = intersection_cnt / union_cnt
    # print(similarity_percent)
    answer = int(similarity_percent * 65536 // 1)
    
    return answer



# 2 정답

def solution(str1, str2):
    arr1 = []  
    arr2 = []
    # 두 str 순회하면서 알파벳만 추출 후 소문자로 변경 후 arr에 넣어줌
    for i in range(len(str1) - 1):
        s = str1[i:i+2]
        if s.isalpha():
            s = s.lower()
            arr1.append(s)
    
    for i in range(len(str2) - 1):
        s = str2[i:i+2]
        if s.isalpha():
            s = s.lower()
            arr2.append(s)  
    # print(arr1, arr2)
    
    # list에 중복되지 않게 넣어줌 (set처럼)
    union_list = []
    for s1 in arr1:
        if s1 not in union_list:
            union_list.append(s1)
    for s2 in arr2:
        if s2 not in union_list:
            union_list.append(s2)
    
    # 둘 다 비어있으면 공집합이므로 65536 출력
    if len(union_list) == 0:
        return 65536
    

    # 합집합 리스트 순회하면서 둘 다 가지고 있을 때, 아닐 때를 나누어 각각 교집합/합집합 cnt에 넣어줌
    intersection_cnt = 0
    union_cnt = 0
    for s in union_list:
        cnt1 = arr1.count(s)
        cnt2 = arr2.count(s)
        print(s, cnt1, cnt2)
        
        if cnt1 >= 1 and cnt2 >= 1:
            min_cnt = min(cnt1, cnt2)
            max_cnt = max(cnt1, cnt2)
            
            intersection_cnt += min_cnt
            union_cnt += max_cnt
        
        else:
            max_cnt = max(cnt1, cnt2)
            union_cnt += max_cnt
    
    similarity_percent = intersection_cnt / union_cnt
    # print(similarity_percent)
    # 소수점 아래 버리고 정수화
    answer = int(similarity_percent * 65536 // 1)
    
    return answer

