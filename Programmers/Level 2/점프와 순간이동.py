# <Idea>
# 순간이동이 *2를 하는 것에 주목.
# 2로 나누다가 홀수를 만나면 -1 해주고 건전지 소비량 +1 해줌

# 1
def solution(n):
    cnt = 0
    while True:
        if n == 0:
            break
        
        if n % 2 == 0:
            n = n // 2
            
        else:
            n = n - 1
            cnt += 1        
    
    return cnt



# 2 이중 while문 넣어주기
def solution(n):
    cnt = 0
    while True:
        if n == 0:
            break
        
				# 이 부분을 넣어줘서 바깥쪽 while문 여러번 안 거칠 수 있게
        while n % 2 == 0:
            n = n // 2
            
        else:
            n = n - 1
            cnt += 1        
    
    return cnt


# 3 개쩌는 풀이
def solution(n):
    return list(bin(n)).count('1')