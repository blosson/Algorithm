# 기본적인 아이디어는 숫자를 str형태로 바꿔서 조작하게 쉽게 만들어주는 것.
# 한 자리 숫자와 두 자리 숫자를 잘 구별해서 적절히 덧셈해서 가져오는 것이 중요했다.
# 그리고 문제를 잘 읽기! (앞에 0을 붙인다는 말이 무슨 뜻인지 몰랐는데 말그대로 str으로 이해하면 되는 거였다..)

# --- 아래 주석처럼 int로도 풀 수 있었음 (몫, 나머지 개념으로)

# N = int(input())
# cur = N
# cnt = 0
# while True:
#     sum_val = (cur//10) + (cur%10)
#     cur= (cur%10) * 10 + (sum_val % 10)
#     cnt += 1
#     if N == cur:
#         break
# print(cnt)

n = input()
original_n = n

if int(n) < 10:
    n = '0'+ n

cnt = 0
while True:

    if int(original_n) < 10:
        sum = str(int(n[0]) + int(n[1]))
        if int(sum) < 10:
            n = n[1] + sum[0]
        else:
            n = n[1] + sum[1]

        # print(n)
        cnt += 1
        if n == '0' + original_n:
            break
        
    else:  # 처음 숫자가 10~99일 때
        sum = str(int(n[0]) + int(n[1]))
        if int(sum) < 10:
            n = n[1] + sum[0]
        else:
            n = n[1] + sum[1]

        # print(n)
        cnt += 1
        if n == original_n:
            break

print(cnt)


