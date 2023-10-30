def solution(d, budget):
    d.sort()
    answer = 0
    money = 0
    for i in d:
        if money + i <= budget:
            money += i
            answer += 1
        else:
            break
    return answer