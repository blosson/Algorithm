# 112ms
'''
맨 처음 조건대로 길이, 숫자합, 사전순으로 풀려다가 너무 까다로워서 어떻게 하지 하다가.. 람다함수를 찾아보고 알게됨.
역시 인간은 도구를 사용할 줄 알아야...
'''

def sum_num(serial_num):            # 각자의 숫자 합 구하는 함수
    result = 0                      # 숫자합
    for i in serial_num:            
        if i.isdigit():             # 문자가 아니고 숫자면 (지난 번 준형이형 풀이에서 아이디어 떠올림)
            result += int(i)

    return result                   # 숫자합 return

N = int(input())                    
serial_nums = []
for _ in range(N):                  # 시리얼 넘버들을 리스트에 넣어준다.
    serial_nums.append(input())

serial_nums.sort(key=lambda x:(len(x), sum_num(x), x))      # 람다함수로 길이, 숫자합, 사전순으로 정렬 (사전순은 그냥 원래 sort하면 됨)
for serial_num in serial_nums:                              # 하나씩 정렬한대로 출력
    print(serial_num)                       
