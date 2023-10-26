# <IDEA>
# - 이중 for문을 돌리면서 자기 자신보다 큰 숫자가 나오면 그 숫자까지의 인덱스 차이를 계산
# - for문 끝까지 돌렸는데도 없으면 마지막 인덱스 - 자신의 인덱스 만큼을 반환
# - 100,000이니 시간초과 생각하기

def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                seconds = j - i
                answer.append(seconds)
                # print(seconds)
                break
            
            if (j == len(prices) - 1):
                seconds = (len(prices) - 1) - i
                answer.append(seconds)
                # print(seconds)
                
    return answer