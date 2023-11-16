def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        cnt = 0
        root_num = int((num ** 0.5) // 1)
    
        for i in range(1, root_num + 1):
            if not (num % i):
                cnt += 2
                if i ** 2 == num:
                    cnt -= 1
        if cnt % 2:
            answer -= num
        else:
            answer += num
                        
    return answer