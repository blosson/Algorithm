# <IDEA>
# 1. 단순 계산을 통해 규칙을 찾기
#     - 다음 라운드의 번호 : 짝수면 - 2로 나눈 몫, 홀수면 2로 나눈 몫 + 1
# 2. while문을 돌려서 A와 B의 번호가 몫이 1차이 나고, 나머지가 1차이나면 같은 대진에 있는 것 (각각 a>b, b>a 경우 각각 처리해줄 것)
#     - 2, 3은 몫이 같으므로 안됨 / 3,4 는 몫이 다르고 나머지가 1차이나므로 가능
#     - round를 cnt해서 출력


# 1  내 풀이
def solution(n,a,b):
    
    round = 1
    while True:
        # a가 b보다 클 경우
        if a > b:
            # 2로 나눈 몫이 1 차이나고 나머지도 1 차이나면 같은 대진표이므로 break
            if (a - b == 1) and ((a // 2) - (b // 2)) == 1:
                break
            # 같은 대진표에 있지 않으면 다음 라운드 이동 (다음 번호 계산)
            else:
                round += 1
                if a % 2 == 0:
                    a = a // 2
                else:
                    a = a // 2 + 1
                
                if b % 2 == 0:
                    b = b // 2
                else:
                    b = b // 2 + 1
        
        # b가 a보다 클 경우
        else:
            # 2로 나눈 몫이 1 차이나고 나머지도 1 차이나면 같은 대진표이므로 break
            if (b - a == 1) and ((b // 2) - (a // 2)) == 1:
                break
            # 같은 대진표에 있지 않으면 다음 라운드 이동 (다음 번호 계산)
            else:
                round += 1
                if a % 2 == 0:
                    a = a // 2
                else:
                    a = a // 2 + 1
                
                if b % 2 == 0:
                    b = b // 2
                else:
                    b = b // 2 + 1     
        
        
    return round




----
# 2 멋진 풀이
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

# 홀수 대 짝수가 1, 2가 될 수 있고, 2, 3이 될 수 있습니다. 
# 이때 1, 2는 지금 붙지만 2, 3은 다음 번에 붙습니다. 
# 그래서 이 두 쌍을 나누는 단순한 방법으로 1을 더하고 몫을 구하는 //2를 한거죠. 
# 만약 그냥 //2를 하거나 1을 빼고 //2를 하면 다음 번에 붙는 2, 3이 이번에 붙는 거로 되니까요


# 3 abs 사용 풀이 (a, b = b, a 아이디어!)
def solution(n, a, b):
    result = 1
    if a > b:
        a, b = b, a
    if a % 2 and abs(a-b) == 1:
            return result
    while True:
        if a % 2:
            a = a // 2 +1
        else:
            a = a // 2
        if b % 2:
            b = b // 2 + 1
        else:
            b = b // 2
        result += 1
        if a % 2 and abs(a-b) == 1:
            return result