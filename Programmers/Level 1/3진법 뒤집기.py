def solution(n):
    answer = ''
    cnt = 0
    num = n
    # 3진수로 몇자리인지 계산 (3의 몇제곱까지 있는지)
    while num >= 3:
        if num // 3 >= 1:
            cnt += 1
            num /= 3
    
    # 10진수를 3진수로 나타내기 (위쪽 자리부터 차례로 계산해주기)
    for i in range(-cnt, 1):
        if n >= 2 * (3 ** -i):
            answer += '2'
            n = n % (2 * (3 ** -i))
        elif n >= (3 ** -i):
            answer += '1'
            n = n % (3 ** -i)
        else:
            answer += '0'     
  
    # 뒤집지 않고 그냥 for문 돌리면 인덱스 조정하기 쉬우므로 이렇게 해줌
    final_answer = 0
    for i in range(0, len(answer)):
        final_answer += int(answer[i]) * (3 ** i)
         
    return final_answer


-----
# 개인적으로 깔끔하다고 생각한 다른 사람 풀이
def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer