#1 TC 1번 시간초과
# 수학적 지식이 필요하므로 그리 좋은 문제는 아닌듯

from itertools import combinations

def solution(clothes):
    # 의상 카테고리별로 딕셔너리에 넣어주기 (중복된 게 없으니 숫자로 넣어줘도 무방)
    outfit_dict = {}
    for cloth in clothes:
        if cloth[1] not in outfit_dict:
            outfit_dict[cloth[1]] = 1
        else:
            outfit_dict[cloth[1]] += 1
        # print(outfit_dict)
    
    # 각 카테고리별로 몇개씩 의상이 있는지 리스트에 넣어주기
    cnt_list = []
    for i in outfit_dict:
        cnt_list.append(outfit_dict[i])
    # print(cnt_list)
    
    # 카테고리 개수 
    category_cnt = len(outfit_dict)
    
    answer = 0
    for i in range(1, category_cnt+1):
        # 조합으로 경우의 수 세기
        comb_list = list(combinations(cnt_list, i))
        # print(comb_list)
        
        # 의상이 1개일 때는 cnt_list를 더해주면 경우의 수가 나옴
        if i == 1:
            answer += sum(cnt_list)
        
        # 2개 이상일 때는 경우의 수 중에서 각 경우의 수를 곱해서 더해주면 됨
        else:
            for comb in comb_list:
                cnt = 1
                for num in comb:
                    cnt *= num
                answer += cnt
    
    return answer


-----
# 괜찮은 풀이
def solution(clothes):

    dic = {}
    for i in clothes:
        if i[1] in dic:  #카테고리 이미 있으면 개수 추가 
            dic[i[1]]+=1
        else: #카테고리 없으면 1로 초기화 
            dic[i[1]]=1

    values = dic.values()
    print('values',values) # 가지의 수, 키의 값들만 
    
    sum = 1
    
    for c in values: #조합수 구하는 식, 키의 값들을 돌면서 
        sum*=(c+1) # 안입는 경우까지 고려해서 +1로 계산해서 곱해줌 
    sum-=1 # 문제에서 최소 한개는 입으니 모두 안입는 경우 빼야됨 

    return sum