#1 #1 7041 --- 입력값으로 받는 방법
#2 어떻게 숫자와 무관한 str을 숫자처럼 정렬시키는 규칙을 만들지?
# 후보1 : (딕셔너리 숫자:str 연결)


'''num_dic = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 
6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}

num_list = ['TWO', 'NIN', 'TWO', 'TWO', 'FIV', 'FOR', 'ZRO', 'EGT']

for i in range(len(num_list)):'''


# 도저히 못 풀겠어서 일단 다른 반 친구들 코드로 올리고 더 고민해서 풀어보겠습니다!

# 인덱스 찾기 함수 정의
def myindex(list, word):
    for i in range(len(list)):
        if list[i] == word:
            return i
# 리스트 내의 숫자를 정렬하는 함수 정의
def mysort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for repeat in range(int(input())):
    TC, N = input().split()
    word_list = list(input().split())
    for i in range(int(N)):
        word_list[i] = myindex(num, word_list[i])
    num_list = mysort(word_list)
    for j in range(len(num_list)):
        num_list[j] = num[num_list[j]]        
    print(TC)
    print(' '.join(num_list))