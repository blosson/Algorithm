# <IDEA>
# 1. idx 1번 이후의 홀수 음식은 -1해서 짝수로 맞춰줘야함 (같은 음식 양 조절)
# 2. 물을 제외하고 모든 음식을 2로 나눠서 배열에 넣어줌
# 3. A 배열을 reverse함 [::-1] → B
# 4. A배열 + [0] + B배열
# 5. str형태로 출력


def solution(food):
    answer = ''
    # idx 0을 제외한 인덱스에서 홀수일 경우 짝수로 바꿔주고, 2로 나눠줌
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
            food[i] = food[i] // 2
        else:
            food[i] = food[i] // 2
    # print(food)
    
    # 왼쪽에서 오는 푸드 파이터 음식 str에 더해주기
    for i in range(1, len(food)):
        cnt = food[i]
        while cnt:
            answer = answer + str(i)
            cnt -= 1
        # print(answer)
    
    # 물 str에 더해주기
    answer = answer + '0'
    
    # 오른쪽에서 오는 푸드 파이터 음식 str에 더해주기
    for i in range(len(food)-1, 0, -1):
        cnt = food[i]
        while cnt:
            answer = answer + str(i)
            cnt -= 1
  
    return answer